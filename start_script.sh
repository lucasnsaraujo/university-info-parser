#!/bin/zsh
python main.py
cd react-website/website
yarn start
ngrok http 3001
