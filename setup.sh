mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
\n\
[theme]
primaryColor = '#d0fcff'\n\
backgroundColor = '#00172B'\n\
secondaryBackgroundColor = '0064a0'\n\
textColor = '#fff'\n\
font = 'sans serif'\n\
" > ~/.streamlit/config.toml