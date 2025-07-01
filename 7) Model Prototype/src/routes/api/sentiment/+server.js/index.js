import fetch from 'node-fetch';

export async function POST({ request }) {
  const { text } = await request.json();
  const HF_TOKEN = process.env.HF_TOKEN;
  const apiUrl = 'https://api-inference.huggingface.co/models/u-kuro/Thesis-2024-U.S.-Presidential-Election-Sentiment-Analysis';

  const r = await fetch(apiUrl, {
    headers: { Authorization: `Bearer ${HF_TOKEN}` },
    method:   'POST',
    body:     JSON.stringify({ inputs: text }),
  });

  if (!r.ok) {
    const err = await r.json();
    return new Response(JSON.stringify({ error: err }), { status: 500 });
  }

  const [out] = await r.json();
  return new Response(JSON.stringify(out), { status: 200 });
}
