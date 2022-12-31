<script>
  let rand = -1;
  let url = "";
  function getRand() {
    fetch("./rand")
      .then(d => d.text())
      .then(d => (rand = d));
  }
  function crawlURL() {
    fetch("./crawl",{ headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "POST",
    body: JSON.stringify({seed: url, depth: 5})})
      .then(d => d.text())
      .then(d => (rand = d));
  }
</script>
<input bind:value={url}>
<button on:click={getRand}>Get a random number</button>
<button on:click={crawlURL}>Crawl URL</button>

<pre>{rand}</pre>
