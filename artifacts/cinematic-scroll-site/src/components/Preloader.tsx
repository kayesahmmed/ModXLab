import { motion, AnimatePresence } from "motion/react";
import { useEffect, useState } from "react";

export default function Preloader({ progress }: { progress: number }) {
  const [show, setShow] = useState(true);

  useEffect(() => {
    if (progress >= 100) {
      const timer = setTimeout(() => setShow(false), 500); // give it a small delay before hiding
      return () => clearTimeout(timer);
    }
  }, [progress]);

  return (
    <AnimatePresence>
      {show && (
        <motion.div
          key="preloader"
          initial={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.8, ease: "easeInOut" }}
          className="fixed inset-0 z-[99999] bg-[#0A0A0A] flex flex-col items-center justify-center overflow-hidden"
        >
          {/* Animated Background Orbs */}
          <motion.div
            animate={{
              scale: [1, 1.2, 1],
              opacity: [0.3, 0.5, 0.3],
            }}
            transition={{
              duration: 4,
              repeat: Infinity,
              ease: "easeInOut",
            }}
            className="absolute w-[40vw] h-[40vw] max-w-[400px] max-h-[400px] rounded-full blur-[100px] opacity-40 bg-gradient-to-r from-[#2790FF] to-[#16CF83] top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 pointer-events-none"
          />

          <div className="relative z-10 flex flex-col items-center gap-8">
            {/* Logo Image */}
            <motion.div
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ duration: 0.5 }}
            >
              <img
                src="/loading_icon.png"
                alt="ModX Lab"
                className="w-32 h-32 sm:w-40 sm:h-40 object-contain drop-shadow-[0_0_20px_rgba(22,207,131,0.5)]"
                onError={(e) => {
                  // Fallback if image not uploaded yet
                  e.currentTarget.style.display = 'none';
                }}
              />
            </motion.div>

            {/* Glowing Percentage */}
            <div className="flex flex-col items-center gap-4">
              <div className="font-['Orbitron',sans-serif] font-black text-4xl sm:text-5xl text-transparent bg-clip-text bg-gradient-to-r from-[#16CF83] to-[#2790FF]">
                {progress}%
              </div>
              
              {/* Progress Bar Container */}
              <div className="w-48 sm:w-64 h-1.5 rounded-full bg-white/10 overflow-hidden relative shadow-[0_0_10px_rgba(255,255,255,0.1)]">
                {/* Progress Bar Fill */}
                <motion.div
                  className="absolute top-0 left-0 h-full bg-gradient-to-r from-[#16CF83] to-[#2790FF]"
                  initial={{ width: "0%" }}
                  animate={{ width: `${progress}%` }}
                  transition={{ ease: "linear", duration: 0.2 }}
                  style={{ boxShadow: "0 0 10px rgba(22,207,131,0.8)" }}
                />
              </div>
              
              <div className="text-xs font-bold text-white/50 uppercase tracking-[0.2em] animate-pulse">
                Loading Sequence
              </div>
            </div>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
