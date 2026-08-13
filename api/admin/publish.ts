export default async function handler(req: any, res: any) {
  // CORS setup
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader('Access-Control-Allow-Headers', 'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version');

  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  const { GITHUB_TOKEN } = process.env;
  if (!GITHUB_TOKEN) {
    return res.status(500).json({ error: 'GITHUB_TOKEN environment variable is not set in Vercel.' });
  }

  const { allData } = req.body;
  if (!allData) {
    return res.status(400).json({ error: 'No data provided.' });
  }

  const owner = 'kayesahmmed';
  const repo = 'ModXLab';
  let branch = 'main';

  try {
    // 1. Get the current commit (try main first, fallback to master)
    let refRes = await fetch(`https://api.github.com/repos/${owner}/${repo}/git/ref/heads/${branch}`, {
      headers: { Authorization: `Bearer ${GITHUB_TOKEN}` }
    });
    
    if (!refRes.ok) {
        branch = 'master';
        refRes = await fetch(`https://api.github.com/repos/${owner}/${repo}/git/ref/heads/${branch}`, {
            headers: { Authorization: `Bearer ${GITHUB_TOKEN}` }
        });
        if (!refRes.ok) {
           throw new Error('Could not get branch ref for main or master. Please check your GitHub repository and token permissions.');
        }
    }
    const refData = await refRes.json();
    const latestCommitSha = refData.object.sha;

    // 2. Get the commit's tree
    const commitRes = await fetch(`https://api.github.com/repos/${owner}/${repo}/git/commits/${latestCommitSha}`, {
      headers: { Authorization: `Bearer ${GITHUB_TOKEN}` }
    });
    const commitData = await commitRes.json();
    const baseTreeSha = commitData.tree.sha;

    // 3. Create the blobs and tree items
    const treeItems = [];
    for (const [key, data] of Object.entries(allData)) {
      if (!data) continue;
      
      const content = JSON.stringify(data, null, 2);
      
      const blobRes = await fetch(`https://api.github.com/repos/${owner}/${repo}/git/blobs`, {
        method: 'POST',
        headers: { 
          Authorization: `Bearer ${GITHUB_TOKEN}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content, encoding: 'utf-8' })
      });
      const blobData = await blobRes.json();
      
      treeItems.push({
        path: `artifacts/cinematic-scroll-site/public/data/${key}.json`,
        mode: '100644',
        type: 'blob',
        sha: blobData.sha
      });
    }

    // Also update version.json
    const versionContent = JSON.stringify({
        version: "1.0.0",
        updatedAt: new Date().toISOString(),
        versions: {
            downloads: Date.now().toString(),
            faqs: Date.now().toString(),
            reviews: Date.now().toString(),
            nav: Date.now().toString(),
            settings: Date.now().toString()
        }
    }, null, 2);
    
    const versionBlobRes = await fetch(`https://api.github.com/repos/${owner}/${repo}/git/blobs`, {
        method: 'POST',
        headers: { 
            Authorization: `Bearer ${GITHUB_TOKEN}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content: versionContent, encoding: 'utf-8' })
    });
    const versionBlobData = await versionBlobRes.json();
    treeItems.push({
        path: `artifacts/cinematic-scroll-site/public/data/version.json`,
        mode: '100644',
        type: 'blob',
        sha: versionBlobData.sha
    });

    // 4. Create new tree
    const treeRes = await fetch(`https://api.github.com/repos/${owner}/${repo}/git/trees`, {
      method: 'POST',
      headers: { 
        Authorization: `Bearer ${GITHUB_TOKEN}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        base_tree: baseTreeSha,
        tree: treeItems
      })
    });
    const treeData = await treeRes.json();
    const newTreeSha = treeData.sha;

    // 5. Create new commit
    const newCommitRes = await fetch(`https://api.github.com/repos/${owner}/${repo}/git/commits`, {
      method: 'POST',
      headers: { 
        Authorization: `Bearer ${GITHUB_TOKEN}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        message: 'Admin Panel: Auto-publish data updates from Vercel dashboard',
        tree: newTreeSha,
        parents: [latestCommitSha]
      })
    });
    const newCommitData = await newCommitRes.json();
    const newCommitSha = newCommitData.sha;

    // 6. Update reference
    const patchRes = await fetch(`https://api.github.com/repos/${owner}/${repo}/git/refs/heads/${branch}`, {
      method: 'PATCH',
      headers: { 
        Authorization: `Bearer ${GITHUB_TOKEN}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        sha: newCommitSha,
        force: false
      })
    });
    
    if (!patchRes.ok) {
        throw new Error('Failed to update branch reference.');
    }

    return res.status(200).json({ success: true, message: 'Published to GitHub successfully! Vercel is now deploying.' });
  } catch (error: any) {
    return res.status(500).json({ error: error.message });
  }
}
