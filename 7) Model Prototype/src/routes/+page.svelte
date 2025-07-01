<script>
  let text = '', resp = null, loading = false;

  async function analyze() {
    loading = true;
    resp = null;
    try {
      const r = await fetch('/api/sentiment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
      });
      resp = await r.json();
    } catch (e) {
      resp = { error: e.message };
    }
    loading = false;
  }
</script>

<main class="p-8 max-w-xl mx-auto">
  <h1 class="text-2xl mb-4">📝 Sentiment Checker</h1>
  <textarea bind:value={text} rows="4" class="w-full p-2 border rounded mb-4" ></textarea>
  <button on:click={analyze} disabled={!text || loading}
          class="px-4 py-2 bg-blue-600 text-white rounded">
    {#if loading}Processing…{:else}Analyze{/if}
  </button>

  {#if resp}
    {#if resp.error}
      <p class="text-red-500 mt-4">Error: {resp.error}</p>
    {:else}
      <div class="mt-4">
        <p>Label: <strong>{resp.label}</strong></p>
        <p>Confidence: {(resp.score * 100).toFixed(1)}%</p>
      </div>
    {/if}
  {/if}
</main>