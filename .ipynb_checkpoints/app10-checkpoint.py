{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, jsonify\n",
    "\n",
    "justice_league_members = [\n",
    "    {\"superhero\": \"Aquaman\", \"real_name\": \"Arthur Curry\"},\n",
    "    {\"superhero\": \"Batman\", \"real_name\": \"Bruce Wayne\"},\n",
    "    {\"superhero\": \"Cyborg\", \"real_name\": \"Victor Stone\"},\n",
    "    {\"superhero\": \"Flash\", \"real_name\": \"Barry Allen\"},\n",
    "    {\"superhero\": \"Green Lantern\", \"real_name\": \"Hal Jordan\"},\n",
    "    {\"superhero\": \"Superman\", \"real_name\": \"Clark Kent/Kal-El\"},\n",
    "    {\"superhero\": \"Wonder Woman\", \"real_name\": \"Princess Diana\"}\n",
    "]\n",
    "\n",
    "#################################################\n",
    "# Flask Setup\n",
    "#################################################\n",
    "app = Flask(__name__)\n",
    "#################################################\n",
    "# Flask Routes\n",
    "#################################################\n",
    "\n",
    "@app.route(\"/api/v1.0/justice-league\")\n",
    "def justice_league():\n",
    "    \"\"\"Return the justice league data as json\"\"\"\n",
    "\n",
    "    return jsonify(justice_league_members)\n",
    "\n",
    "\n",
    "@app.route(\"/\")\n",
    "def welcome():\n",
    "    return (\n",
    "        f\"Welcome to the Justice League API!<br/>\"\n",
    "        f\"Available Routes:<br/>\"\n",
    "        f\"/api/v1.0/justice-league<br/>\"\n",
    "        f\"/api/v1.0/justice-league/Arthur%20Curry<br/>\"\n",
    "        f\"/api/v1.0/justice-league/Bruce%20Wayne<br/>\"\n",
    "        f\"/api/v1.0/justice-league/Victor%20Stone<br/>\"\n",
    "        f\"/api/v1.0/justice-league/Barry%20Allen<br/>\"\n",
    "        f\"/api/v1.0/justice-league/Hal%20Jordan<br/>\"\n",
    "        f\"/api/v1.0/justice-league/Clark%20Kent/Kal-El<br/>\"\n",
    "        f\"/api/v1.0/justice-league/Princess%20Diana\"\n",
    "    )\n",
    "\n",
    "\n",
    "@app.route(\"/api/v1.0/justice-league/<real_name>\")\n",
    "def justice_league_character(real_name):\n",
    "    \"\"\"Fetch the Justice League character whose real_name matches\n",
    "       the path variable supplied by the user, or a 404 if not.\"\"\"\n",
    "\n",
    "    canonicalized = real_name.replace(\" \", \"\").lower()\n",
    "    for character in justice_league_members:\n",
    "        search_term = character[\"real_name\"].replace(\" \", \"\").lower()\n",
    "\n",
    "        if search_term == canonicalized:\n",
    "            return jsonify(character)\n",
    "\n",
    "    return jsonify({\"error\": f\"Character with real_name {real_name} not found.\"}), 404\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
