// Intakes scoreData and generates table rows in score-container tbody.
function generateScoreRows(scoreData)
{
    var tbody = document.getElementById('score-container');

    // Clear existing rows
    tbody.innerHTML = '';

    for (z = 0; z < scoreData.length; z++)
    {
        // Create containing row
        var row = document.createElement('tr');
        row.className = 'score-row';

        // Create and append rank cell
        var rank = document.createElement('td');
        if (z == 0) { rank.textContent = medals[0]; }
        else if (z == 1) { rank.textContent = medals[1]; }
        else if (z == 2) { rank.textContent = medals[2]; }
        else { rank.textContent = z + 1; }
        row.appendChild(rank);

        // Create and append score cell
        var score = document.createElement('td');
        score.textContent = scoreData[z][1].score;
        row.appendChild(score);

        // Create and append name cell
        var name = document.createElement('td');
        name.textContent = scoreData[z][0];
        row.appendChild(name);

        // Create and append games cell
        var games = document.createElement('td');
        games.textContent = scoreData[z][1].n;
        row.appendChild(games);

        // Add eventlistener to navigate to assiocated user's page
        row.addEventListener('click', function()
        {
            window.location.href = "user.html?name=" + this.cells[2].textContent;
        });

        // Append containing row to tbody
        tbody.appendChild(row);
    }
}
