import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

const css_file = "index.min.css";

export default defineConfig({
  plugins: [react()],
  publicDir: "./public",
  build: {
    rollupOptions: {
      output: {
        assetFileNames: (file) => {
          return `assets/css/${css_file}`;
        },
        entryFileNames: (file) => {
          return `assets/js/[name].min.js`;
        },
      },
    },
  },
});
