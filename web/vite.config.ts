import path from "path"
import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: { alias: { "@": path.resolve(__dirname, "./src") } },
  // FastAPI serves the built app from /static and the API from /api
  base: "/static/",
  build: { outDir: "../app/static", emptyOutDir: true },
  server: { proxy: { "/api": process.env.API_URL ?? "http://localhost:8000" } },
})
