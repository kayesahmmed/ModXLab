type Listener = (progress: number) => void;
const listeners = new Set<Listener>();
let currentProgress = 0;

export const preloaderEvents = {
  setProgress(val: number) {
    currentProgress = Math.min(100, Math.max(0, val));
    listeners.forEach((fn) => fn(currentProgress));
  },
  getProgress() {
    return currentProgress;
  },
  subscribe(fn: Listener) {
    listeners.add(fn);
    fn(currentProgress);
    return () => {
      listeners.delete(fn);
    };
  }
};
