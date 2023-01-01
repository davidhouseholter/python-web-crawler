<script>
  let rand = -1;
  let url = "";
  function getRand() {
    fetch("./rand")
      .then(d => d.text())
      .then(d => (rand = d));
  }
  function crawlURL(type = 1) {
    fetch("./tasks",{ headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "POST",
    body: JSON.stringify({seed: url, depth: 0, type: 1})})
      .then(d => d.json())
      .then(d => {rand = JSON.stringify(d.data); getStatus(d.data.task_id);});
  }
  function  getStatus(taskID) {
     fetch(`/tasks/${taskID}`,{ headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "GET"})
      .then(d => d.json())
      .then(res => {
        console.log(res.data)
        const taskStatus = res.data.task_status;
        if (taskStatus === 'finished' || taskStatus === 'failed') return false;
        setTimeout(function() {
          getStatus(res.data.task_id);
        }, 1000);
      });
  }
</script>
<input bind:value={url}>
<button on:click={getRand}>Get a random number</button>
<button on:click={crawlURL}>Crawl URL</button>

<pre>{rand}</pre>
