<!doctype html>
<html lang="fa">
<head>
<meta charset="utf-8">
<title>Live Logs</title>
<style>
body { background:#111; color:#0f0; font-family: monospace; }
pre { white-space: pre-wrap; }
</style>
</head>
<body>

<h3>Live Logs</h3>
<pre id="logs">در حال اتصال...</pre>

<script>
async function loadLogs() {
  const res = await fetch('requests.log?_=' + Date.now());
  const text = await res.text();
  document.getElementById('logs').textContent = text;
}

setInterval(loadLogs, 2000);
loadLogs();
</script>

</body>
</html>
