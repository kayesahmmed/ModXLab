import { motion, AnimatePresence } from "motion/react";
import { useEffect, useState } from "react";
import { useLenis } from "lenis/react";

export default function Preloader({ progress }: { progress: number }) {
  const [show, setShow] = useState(true);
  const displayProgress = Math.min(Math.max(Math.round(progress), 0), 100);
  const lenis = useLenis();

  useEffect(() => {
    if (show) {
      document.body.style.overflow = "hidden";
      try {
        if (lenis && typeof (lenis as any).stop === "function") {
          (lenis as any).stop();
        } else if (typeof (window as any).lenis?.stop === "function") {
          (window as any).lenis.stop();
        }
      } catch (e) {
        // Safe guard against non-standard scroll instances
      }
    } else {
      document.body.style.overflow = "";
      try {
        if (lenis && typeof (lenis as any).start === "function") {
          (lenis as any).start();
        } else if (typeof (window as any).lenis?.start === "function") {
          (window as any).lenis.start();
        }
      } catch (e) {
        // Safe guard against non-standard scroll instances
      }
    }
    return () => {
      document.body.style.overflow = "";
      try {
        if (lenis && typeof (lenis as any).start === "function") {
          (lenis as any).start();
        } else if (typeof (window as any).lenis?.start === "function") {
          (window as any).lenis.start();
        }
      } catch (e) {
        // Safe guard against non-standard scroll instances
      }
    };
  }, [show, lenis]);

  useEffect(() => {
    if (progress >= 100) {
      const timer = setTimeout(() => setShow(false), 450);
      return () => clearTimeout(timer);
    }
    return undefined;
  }, [progress]);

  return (
    <AnimatePresence>
      {show && (
        <motion.div
          key="preloader"
          initial={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.6, ease: "easeInOut" }}
          className="fixed inset-0 z-[99999] bg-[#0A0A0A] flex flex-col items-center justify-center overflow-hidden select-none"
        >
          {/* Animated Background Orbs */}
          <motion.div
            animate={{
              scale: [1, 1.25, 1],
              opacity: [0.25, 0.45, 0.25],
            }}
            transition={{
              duration: 3.5,
              repeat: Infinity,
              ease: "easeInOut",
            }}
            className="absolute w-[45vw] h-[45vw] max-w-[420px] max-h-[420px] rounded-full blur-[100px] bg-gradient-to-r from-[#2790FF] to-[#16CF83] top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 pointer-events-none"
          />

          <div className="relative z-10 flex flex-col items-center gap-7">
            {/* Logo Image */}
            <motion.div
              initial={{ scale: 0.85, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ duration: 0.4 }}
              className="flex flex-col items-center gap-2"
            >
              <img
                src="/website-logo.png"
                alt="ModX Lab"
                className="w-24 h-24 sm:w-32 sm:h-32 object-contain drop-shadow-[0_0_25px_rgba(22,207,131,0.55)]"
                onError={(e) => {
                  e.currentTarget.style.display = 'none';
                }}
              />
              <span className="font-['Orbitron',sans-serif] font-black text-xl sm:text-2xl tracking-widest text-transparent bg-clip-text bg-gradient-to-r from-[#16CF83] to-[#2790FF]">
                MODX LAB
              </span>
            </motion.div>

            {/* Glowing Percentage */}
            <div className="flex flex-col items-center gap-3.5">
              <div className="font-['Orbitron',sans-serif] font-black text-4xl sm:text-5xl text-transparent bg-clip-text bg-gradient-to-r from-[#16CF83] via-[#00E5D1] to-[#2790FF] tracking-wider tabular-nums">
                {displayProgress}%
              </div>
              
              {/* Progress Bar Container */}
              <div className="w-52 sm:w-72 h-2 rounded-full bg-white/10 overflow-hidden relative shadow-[0_0_12px_rgba(255,255,255,0.08)] border border-white/10">
                {/* Progress Bar Fill */}
                <motion.div
                  className="absolute top-0 left-0 h-full bg-gradient-to-r from-[#16CF83] via-[#00E5D1] to-[#2790FF]"
                  initial={{ width: "0%" }}
                  animate={{ width: `${displayProgress}%` }}
                  transition={{ ease: "easeOut", duration: 0.2 }}
                  style={{ boxShadow: "0 0 14px rgba(22,207,131,0.85)" }}
                />
              </div>
              
              <div className="text-[11px] font-extrabold text-white/60 uppercase tracking-[0.25em] animate-pulse mt-1">
                Loading All Resources...
              </div>
            </div>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
