export const checkAndRecordSubmission = (): { allowed: boolean; message?: string } => {
  const now = Date.now();
  const limitWindow = 10 * 60 * 1000; // 10 minutes
  const maxSubmissions = 4;
  
  try {
    const historyJson = localStorage.getItem("user_submission_history");
    let history: number[] = [];
    
    if (historyJson) {
      history = JSON.parse(historyJson);
    }
    
    // Filter out timestamps older than 10 minutes
    history = history.filter(time => now - time < limitWindow);
    
    if (history.length >= maxSubmissions) {
      return { 
        allowed: false, 
        message: "You have reached the maximum limit of 4 submissions. Please try again after 10 minutes or join our Telegram group to share your thoughts." 
      };
    }
    
    // Update history
    history.push(now);
    localStorage.setItem("user_submission_history", JSON.stringify(history));
    
    return { allowed: true };
  } catch (error) {
    console.error("Rate limit check failed", error);
    return { allowed: true }; // Fallback to allow if localStorage is blocked
  }
};
