# pc-streamlit-example

Make sure streamlit is installed

```console
$ python -m pip install streamlit
```

Start the streamlit server

```console
$ streamlit run stac-example.py --browser.serverAddress 0.0.0.0 --server.enableCORS False
```

Open your browser to `https://<JUPYTERHUB_URL>/user/<username>/proxy/8501/`

(the trailing slash is important)


![example screenshot](screenshot.md)
