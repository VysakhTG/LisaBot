if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Tony-stark003/LisaBot.git /LisaBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /LisaBot
fi
cd /Lisabot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
