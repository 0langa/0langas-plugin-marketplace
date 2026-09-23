// Render every round-4 SVG to a 1024x1024 PNG with a transparent background.
import { readFileSync, writeFileSync, readdirSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { Resvg } from "@resvg/resvg-js";

const src = process.argv[2];
const out = process.argv[3];
mkdirSync(out, { recursive: true });
for (const file of readdirSync(src).filter((f) => f.endsWith(".svg"))) {
  const svg = readFileSync(join(src, file), "utf8");
  const png = new Resvg(svg, { fitTo: { mode: "width", value: 1024 }, background: "rgba(0,0,0,0)" }).render().asPng();
  writeFileSync(join(out, file.replace(/\.svg$/, ".png")), png);
  console.log(file, png.length);
}
