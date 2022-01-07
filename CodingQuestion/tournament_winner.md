![image](https://user-images.githubusercontent.com/11685096/148571822-c47b0a83-f59a-4856-907e-345bc5bd3842.png)

Solution
```python
def tournamentWinner(competitions, results):
    # Write your code here.
    team_dict = dict()
	final_team = None
	for home, away in competitions:
		if home not in team_dict.keys():
			team_dict[home] = 0
		if away not in team_dict.keys():
			team_dict[away] = 0
	
	for idx in range(len(competitions)):
		team_dict[competitions[idx][results[idx]-1]] += 3
		print(team_dict)
		if team_dict[competitions[idx][0]] > team_dict[competitions[idx][1]] :
			winner = [competitions[idx][0],team_dict[competitions[idx][0]]]
		else:
			winner = [competitions[idx][1], team_dict[competitions[idx][1]]]
		if final_team is None or final_team[1]< winner[1] :
			final_team = winner
	return final_team[0]

```
