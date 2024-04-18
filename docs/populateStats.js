// Intakes wordleStats and populates DOM with author's stats
function populateStats(wordleStats)
{
    var n = document.getElementById('n');
    var score = document.getElementById('score');
    var offByOneCount = document.getElementById('offByOneCount');
    var offByOneAverage = document.getElementById('offByOneAverage');
    var guess1Count = document.getElementById('guess1Count');
    var guess1Average = document.getElementById('guess1Average');
    var guess2Count = document.getElementById('guess2Count');
    var guess2Average = document.getElementById('guess2Average');
    var guess3Count = document.getElementById('guess3Count');
    var guess3Average = document.getElementById('guess3Average');
    var guess4Count = document.getElementById('guess4Count');
    var guess4Average = document.getElementById('guess4Average');
    var guess5Count = document.getElementById('guess5Count');
    var guess5Average = document.getElementById('guess5Average');
    var guess6Count = document.getElementById('guess6Count');
    var guess6Average = document.getElementById('guess6Average');
    var result1Count = document.getElementById('result1Count');
    var result1Average = document.getElementById('result1Average');
    var result2Count = document.getElementById('result2Count');
    var result2Average = document.getElementById('result2Average');
    var result3Count = document.getElementById('result3Count');
    var result3Average = document.getElementById('result3Average');
    var result4Count = document.getElementById('result4Count');
    var result4Average = document.getElementById('result4Average');
    var result5Count = document.getElementById('result5Count');
    var result5Average = document.getElementById('result5Average');
    var result6Count = document.getElementById('result6Count');
    var result6Average = document.getElementById('result6Average');
    var resultXCount = document.getElementById('resultXCount');
    var resultXAverage = document.getElementById('resultXAverage');
    var currentXLessStreak = document.getElementById('currentXLessStreak');
    var maxXLessStreak = document.getElementById('maxXLessStreak');
    var currentPostStreak = document.getElementById('currentPostStreak');
    var maxPostStreak = document.getElementById('maxPostStreak');
    var currentCombinedStreak = document.getElementById('currentCombinedStreak');
    var maxCombinedStreak = document.getElementById('maxCombinedStreak');

    n.innerHTML = wordleStats['n'];
    score.innerHTML = wordleStats['score'];
    offByOneCount.innerHTML = wordleStats['offByOneCount'];
    offByOneAverage.innerHTML = wordleStats['offByOneAverage'];

    guess1Count.innerHTML = wordleStats['guess1Count'];
    guess1Average.innerHTML = wordleStats['guess1Average'];
    guess2Count.innerHTML = wordleStats['guess2Count'];
    guess2Average.innerHTML = wordleStats['guess2Average'];
    guess3Count.innerHTML = wordleStats['guess3Count'];
    guess3Average.innerHTML = wordleStats['guess3Average'];
    guess4Count.innerHTML = wordleStats['guess4Count'];
    guess4Average.innerHTML = wordleStats['guess4Average'];
    guess5Count.innerHTML = wordleStats['guess5Count'];
    guess5Average.innerHTML = wordleStats['guess5Average'];
    guess6Count.innerHTML = wordleStats['guess6Count'];
    guess6Average.innerHTML = wordleStats['guess6Average'];

    result1Count.innerHTML = wordleStats['result1Count'];
    result1Average.innerHTML = wordleStats['result1Average'];
    result2Count.innerHTML = wordleStats['result2Count'];
    result2Average.innerHTML = wordleStats['result2Average'];
    result3Count.innerHTML = wordleStats['result3Count'];
    result3Average.innerHTML = wordleStats['result3Average'];
    result4Count.innerHTML = wordleStats['result4Count'];
    result4Average.innerHTML = wordleStats['result4Average'];
    result5Count.innerHTML = wordleStats['result5Count'];
    result5Average.innerHTML = wordleStats['result5Average'];
    result6Count.innerHTML = wordleStats['result6Count'];
    result6Average.innerHTML = wordleStats['result6Average'];
    resultXCount.innerHTML = wordleStats['resultXCount'];
    resultXAverage.innerHTML = wordleStats['resultXAverage'];

    currentXLessStreak.innerHTML = wordleStats['currentXLessStreak'];
    maxXLessStreak.innerHTML = wordleStats['maxXLessStreak'];
    currentPostStreak.innerHTML = wordleStats['currentPostStreak'];
    maxPostStreak.innerHTML = wordleStats['maxPostStreak'];
    currentCombinedStreak.innerHTML = wordleStats['currentCombinedStreak'];
    maxCombinedStreak.innerHTML = wordleStats['maxCombinedStreak'];
}