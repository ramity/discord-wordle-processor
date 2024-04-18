// Intakes wordles array and generates wordles to #wordle-container.
function generateWordles(wordles)
{
    var container = document.getElementById('wordle-container');

    // Clear existing rows
    container.innerHTML = '';

    for (var z = 0; z < wordles.length; z++)
    {
        var wordle = document.createElement('div');
        wordle.className = 'wordle-instance px-2 container';

        var guesses = wordles[z].guesses;

        for (var y = 0; y < guesses.length; y++)
        {
            // Create containing row
            var row = document.createElement('div');
            row.className = 'row';

            // Store guess into out of scope memory to consume
            var guess = guesses[y];

            for (var x = 0; x < 5; x++)
            {
                var col = document.createElement('div');
                
                // position
                if (guess.startsWith(greenSquare))
                {
                    col.className = 'col wordle-position';
                    guess = guess.replace(greenSquare, '');
                }
                else if (guess.startsWith(orangeSquare))
                {
                    col.className = 'col wordle-position';
                    guess = guess.replace(orangeSquare, '');
                }

                // present
                else if (guess.startsWith(yellowSquare))
                {
                    col.className = 'col wordle-present';
                    guess = guess.replace(yellowSquare, '');
                }
                else if (guess.startsWith(blueSquare))
                {
                    col.className = 'col wordle-present';
                    guess = guess.replace(blueSquare, '');
                }

                // miss
                else if (guess.startsWith(blackSquare))
                {
                    col.className = 'col wordle-miss';
                    guess = guess.replace(blackSquare, '');
                }
                else if (guess.startsWith(whiteSquare))
                {
                    col.className = 'col wordle-miss';
                    guess = guess.replace(whiteSquare, '');
                }

                // unhandled
                else
                {
                    console.error('unknown');
                    console.log(guesses[y]);
                }

                row.appendChild(col);
            }

            // Append containing row to tbody
            wordle.appendChild(row);
        }

        // Add empty cells
        for (var y = 0; y < 6 - guesses.length; y++)
        {
            var row = document.createElement('div');
            row.className = 'row';

            for (var x = 0; x < 5; x++)
            {
                var col = document.createElement('div');
                col.className = 'col wordle-empty';
                row.appendChild(col);
            }

            // Append containing row to tbody
            wordle.appendChild(row);
        }

        // Add wordle instance to container
        container.appendChild(wordle);
    }
}
