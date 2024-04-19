// Function to calculate the min value of a shared property
function calculateMin(data, property, decimals=1)
{
    if (data.length === 0)
    {
        return 0;
    }

    // Init min Value
    let minValue;
    for (author in data)
    {
        minValue = data[author][property];
        break;
    }

    for (author in data)
    {
        if (data[author].hasOwnProperty(property))
        {
            if (data[author][property] < minValue)
            {
                minValue = data[author][property];
            }
        }
    }

    return Math.round(minValue * (10 ** decimals)) / (10 ** decimals);
}

// Function to calculate the max value of a shared property
function calculateMax(data, property, decimals=1)
{
    if (data.length === 0)
    {
        return 0;
    }

    // Init max Value
    let maxValue;
    for (author in data)
    {
        maxValue = data[author][property];
        break;
    }

    for (author in data)
    {
        if (data[author].hasOwnProperty(property))
        {
            if (data[author][property] > maxValue)
            {
                maxValue = data[author][property];
            }
        }
    }

    return Math.round(maxValue * (10 ** decimals)) / (10 ** decimals);
}


// Function to calculate the average value of a shared property
function calculateAverage(data, property, decimals=1)
{
    let sum = 0;
    let count = 0;

    // Iterate over each object
    for (let key in data)
    {
        if (data.hasOwnProperty(key))
        {
            const obj = data[key];

            // Check if the property exists in the object
            if (obj.hasOwnProperty(property))
            {
                sum += obj[property];
                count++;
            }
        }
    }

    if (count > 0)
    {
        return Math.round(sum / count * (10 ** decimals)) / (10 ** decimals);
    }
    else
    {
        return 0;
    }
}

// Intakes wordleStats and populates DOM with author's stats
function populateStats(author, json)
{
    var wordleStats = json[author];

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

    var nStats = document.getElementById('n-stats');
    var scoreStats = document.getElementById('score-stats');
    var offByOneCountStats = document.getElementById('offByOneCount-stats');
    var offByOneAverageStats = document.getElementById('offByOneAverage-stats');
    var guess1CountStats = document.getElementById('guess1Count-stats');
    var guess1AverageStats = document.getElementById('guess1Average-stats');
    var guess2CountStats = document.getElementById('guess2Count-stats');
    var guess2AverageStats = document.getElementById('guess2Average-stats');
    var guess3CountStats = document.getElementById('guess3Count-stats');
    var guess3AverageStats = document.getElementById('guess3Average-stats');
    var guess4CountStats = document.getElementById('guess4Count-stats');
    var guess4AverageStats = document.getElementById('guess4Average-stats');
    var guess5CountStats = document.getElementById('guess5Count-stats');
    var guess5AverageStats = document.getElementById('guess5Average-stats');
    var guess6CountStats = document.getElementById('guess6Count-stats');
    var guess6AverageStats = document.getElementById('guess6Average-stats');
    var result1CountStats = document.getElementById('result1Count-stats');
    var result1AverageStats = document.getElementById('result1Average-stats');
    var result2CountStats = document.getElementById('result2Count-stats');
    var result2AverageStats = document.getElementById('result2Average-stats');
    var result3CountStats = document.getElementById('result3Count-stats');
    var result3AverageStats = document.getElementById('result3Average-stats');
    var result4CountStats = document.getElementById('result4Count-stats');
    var result4AverageStats = document.getElementById('result4Average-stats');
    var result5CountStats = document.getElementById('result5Count-stats');
    var result5AverageStats = document.getElementById('result5Average-stats');
    var result6CountStats = document.getElementById('result6Count-stats');
    var result6AverageStats = document.getElementById('result6Average-stats');
    var resultXCountStats = document.getElementById('resultXCount-stats');
    var resultXAverageStats = document.getElementById('resultXAverage-stats');
    var currentXLessStreakStats = document.getElementById('currentXLessStreak-stats');
    var maxXLessStreakStats = document.getElementById('maxXLessStreak-stats');
    var currentPostStreakStats = document.getElementById('currentPostStreak-stats');
    var maxPostStreakStats = document.getElementById('maxPostStreak-stats');
    var currentCombinedStreakStats = document.getElementById('currentCombinedStreak-stats');
    var maxCombinedStreakStats = document.getElementById('maxCombinedStreak-stats');

    // min

    var minN = calculateMin(json, 'n', 0);
    var minScore = calculateMin(json, 'score');
    var minOffByOneCount = calculateMin(json, 'offByOneCount', 0);
    var minOffByOneAverage = calculateMin(json, 'offByOneAverage');
    var minGuess1Count = calculateMin(json, 'guess1Count');
    var minGuess1Average = calculateMin(json, 'guess1Average');
    var minGuess2Count = calculateMin(json, 'guess2Count');
    var minGuess2Average = calculateMin(json, 'guess2Average');
    var minGuess3Count = calculateMin(json, 'guess3Count');
    var minGuess3Average = calculateMin(json, 'guess3Average');
    var minGuess4Count = calculateMin(json, 'guess4Count');
    var minGuess4Average = calculateMin(json, 'guess4Average');
    var minGuess5Count = calculateMin(json, 'guess5Count');
    var minGuess5Average = calculateMin(json, 'guess5Average');
    var minGuess6Count = calculateMin(json, 'guess6Count');
    var minGuess6Average = calculateMin(json, 'guess6Average');
    var minResult1Count = calculateMin(json, 'result1Count');
    var minResult1Average = calculateMin(json, 'result1Average');
    var minResult2Count = calculateMin(json, 'result2Count');
    var minResult2Average = calculateMin(json, 'result2Average');
    var minResult3Count = calculateMin(json, 'result3Count');
    var minResult3Average = calculateMin(json, 'result3Average');
    var minResult4Count = calculateMin(json, 'result4Count');
    var minResult4Average = calculateMin(json, 'result4Average');
    var minResult5Count = calculateMin(json, 'result5Count');
    var minResult5Average = calculateMin(json, 'result5Average');
    var minResult6Count = calculateMin(json, 'result6Count');
    var minResult6Average = calculateMin(json, 'result6Average');
    var minResultXCount = calculateMin(json, 'resultXCount');
    var minResultXAverage = calculateMin(json, 'resultXAverage');
    var minCurrentXLessStreak = calculateMin(json, 'currentXLessStreak');
    var minMaxXLessStreak = calculateMin(json, 'maxXLessStreak');
    var minCurrentPostStreak = calculateMin(json, 'currentPostStreak');
    var minMaxPostStreak = calculateMin(json, 'maxPostStreak');
    var minCurrentCombinedStreak = calculateMin(json, 'currentCombinedStreak');
    var minMaxCombinedStreak = calculateMin(json, 'maxCombinedStreak');

    // max

    var maxN = calculateMax(json, 'n', 0);
    var maxScore = calculateMax(json, 'score');
    var maxOffByOneCount = calculateMax(json, 'offByOneCount', 0);
    var maxOffByOneAverage = calculateMax(json, 'offByOneAverage');
    var maxGuess1Count = calculateMax(json, 'guess1Count');
    var maxGuess1Average = calculateMax(json, 'guess1Average');
    var maxGuess2Count = calculateMax(json, 'guess2Count');
    var maxGuess2Average = calculateMax(json, 'guess2Average');
    var maxGuess3Count = calculateMax(json, 'guess3Count');
    var maxGuess3Average = calculateMax(json, 'guess3Average');
    var maxGuess4Count = calculateMax(json, 'guess4Count');
    var maxGuess4Average = calculateMax(json, 'guess4Average');
    var maxGuess5Count = calculateMax(json, 'guess5Count');
    var maxGuess5Average = calculateMax(json, 'guess5Average');
    var maxGuess6Count = calculateMax(json, 'guess6Count');
    var maxGuess6Average = calculateMax(json, 'guess6Average');
    var maxResult1Count = calculateMax(json, 'result1Count');
    var maxResult1Average = calculateMax(json, 'result1Average');
    var maxResult2Count = calculateMax(json, 'result2Count');
    var maxResult2Average = calculateMax(json, 'result2Average');
    var maxResult3Count = calculateMax(json, 'result3Count');
    var maxResult3Average = calculateMax(json, 'result3Average');
    var maxResult4Count = calculateMax(json, 'result4Count');
    var maxResult4Average = calculateMax(json, 'result4Average');
    var maxResult5Count = calculateMax(json, 'result5Count');
    var maxResult5Average = calculateMax(json, 'result5Average');
    var maxResult6Count = calculateMax(json, 'result6Count');
    var maxResult6Average = calculateMax(json, 'result6Average');
    var maxResultXCount = calculateMax(json, 'resultXCount');
    var maxResultXAverage = calculateMax(json, 'resultXAverage');
    var maxCurrentXLessStreak = calculateMax(json, 'currentXLessStreak');
    var maxMaxXLessStreak = calculateMax(json, 'maxXLessStreak');
    var maxCurrentPostStreak = calculateMax(json, 'currentPostStreak');
    var maxMaxPostStreak = calculateMax(json, 'maxPostStreak');
    var maxCurrentCombinedStreak = calculateMax(json, 'currentCombinedStreak');
    var maxMaxCombinedStreak = calculateMax(json, 'maxCombinedStreak');

    // average

    var averageN = calculateAverage(json, 'n', 0);
    var averageScore = calculateAverage(json, 'score');
    var averageOffByOneCount = calculateAverage(json, 'offByOneCount', 0);
    var averageOffByOneAverage = calculateAverage(json, 'offByOneAverage');
    var averageGuess1Count = calculateAverage(json, 'guess1Count');
    var averageGuess1Average = calculateAverage(json, 'guess1Average');
    var averageGuess2Count = calculateAverage(json, 'guess2Count');
    var averageGuess2Average = calculateAverage(json, 'guess2Average');
    var averageGuess3Count = calculateAverage(json, 'guess3Count');
    var averageGuess3Average = calculateAverage(json, 'guess3Average');
    var averageGuess4Count = calculateAverage(json, 'guess4Count');
    var averageGuess4Average = calculateAverage(json, 'guess4Average');
    var averageGuess5Count = calculateAverage(json, 'guess5Count');
    var averageGuess5Average = calculateAverage(json, 'guess5Average');
    var averageGuess6Count = calculateAverage(json, 'guess6Count');
    var averageGuess6Average = calculateAverage(json, 'guess6Average');
    var averageResult1Count = calculateAverage(json, 'result1Count');
    var averageResult1Average = calculateAverage(json, 'result1Average');
    var averageResult2Count = calculateAverage(json, 'result2Count');
    var averageResult2Average = calculateAverage(json, 'result2Average');
    var averageResult3Count = calculateAverage(json, 'result3Count');
    var averageResult3Average = calculateAverage(json, 'result3Average');
    var averageResult4Count = calculateAverage(json, 'result4Count');
    var averageResult4Average = calculateAverage(json, 'result4Average');
    var averageResult5Count = calculateAverage(json, 'result5Count');
    var averageResult5Average = calculateAverage(json, 'result5Average');
    var averageResult6Count = calculateAverage(json, 'result6Count');
    var averageResult6Average = calculateAverage(json, 'result6Average');
    var averageResultXCount = calculateAverage(json, 'resultXCount');
    var averageResultXAverage = calculateAverage(json, 'resultXAverage');
    var averageCurrentXLessStreak = calculateAverage(json, 'currentXLessStreak');
    var averageMaxXLessStreak = calculateAverage(json, 'maxXLessStreak');
    var averageCurrentPostStreak = calculateAverage(json, 'currentPostStreak');
    var averageMaxPostStreak = calculateAverage(json, 'maxPostStreak');
    var averageCurrentCombinedStreak = calculateAverage(json, 'currentCombinedStreak');
    var averageMaxCombinedStreak = calculateAverage(json, 'maxCombinedStreak');

    // Set values

    nStats.innerHTML = minN + "/" + averageN + "/" + maxN;
    scoreStats.innerHTML = minScore + "/" + averageScore + "/" + maxScore;
    offByOneCountStats.innerHTML = minOffByOneCount + "/" + averageOffByOneCount + "/" + maxOffByOneCount;
    offByOneAverageStats.innerHTML = minOffByOneAverage + "/" + averageOffByOneAverage + "/" + maxOffByOneAverage;
    guess1CountStats.innerHTML = minGuess1Count + "/" + averageGuess1Count + "/" + maxGuess1Count;
    guess1AverageStats.innerHTML = minGuess1Average + "/" + averageGuess1Average + "/" + maxGuess1Average;
    guess2CountStats.innerHTML = minGuess2Count + "/" + averageGuess2Count + "/" + maxGuess2Count;
    guess2AverageStats.innerHTML = minGuess2Average + "/" + averageGuess2Average + "/" + maxGuess2Average;
    guess3CountStats.innerHTML = minGuess3Count + "/" + averageGuess3Count + "/" + maxGuess3Count;
    guess3AverageStats.innerHTML = minGuess3Average + "/" + averageGuess3Average + "/" + maxGuess3Average;
    guess4CountStats.innerHTML = minGuess4Count + "/" + averageGuess4Count + "/" + maxGuess4Count;
    guess4AverageStats.innerHTML = minGuess4Average + "/" + averageGuess4Average + "/" + maxGuess4Average;
    guess5CountStats.innerHTML = minGuess5Count + "/" + averageGuess5Count + "/" + maxGuess5Count;
    guess5AverageStats.innerHTML = minGuess5Average + "/" + averageGuess5Average + "/" + maxGuess5Average;
    guess6CountStats.innerHTML = minGuess6Count + "/" + averageGuess6Count + "/" + maxGuess6Count;
    guess6AverageStats.innerHTML = minGuess6Average + "/" + averageGuess6Average + "/" + maxGuess6Average;
    result1CountStats.innerHTML = minResult1Count + "/" + averageResult1Count + "/" + maxResult1Count;
    result1AverageStats.innerHTML = minResult1Average + "/" + averageResult1Average + "/" + maxResult1Average;
    result2CountStats.innerHTML = minResult2Count + "/" + averageResult2Count + "/" + maxResult2Count;
    result2AverageStats.innerHTML = minResult2Average + "/" + averageResult2Average + "/" + maxResult2Average;
    result3CountStats.innerHTML = minResult3Count + "/" + averageResult3Count + "/" + maxResult3Count;
    result3AverageStats.innerHTML = minResult3Average + "/" + averageResult3Average + "/" + maxResult3Average;
    result4CountStats.innerHTML = minResult4Count + "/" + averageResult4Count + "/" + maxResult4Count;
    result4AverageStats.innerHTML = minResult4Average + "/" + averageResult4Average + "/" + maxResult4Average;
    result5CountStats.innerHTML = minResult5Count + "/" + averageResult5Count + "/" + maxResult5Count;
    result5AverageStats.innerHTML = minResult5Average + "/" + averageResult5Average + "/" + maxResult5Average;
    result6CountStats.innerHTML = minResult6Count + "/" + averageResult6Count + "/" + maxResult6Count;
    result6AverageStats.innerHTML = minResult6Average + "/" + averageResult6Average + "/" + maxResult6Average;
    resultXCountStats.innerHTML = minResultXCount + "/" + averageResultXCount + "/" + maxResultXCount;
    resultXAverageStats.innerHTML = minResultXAverage + "/" + averageResultXAverage + "/" + maxResultXAverage;
    currentXLessStreakStats.innerHTML = minCurrentXLessStreak + "/" + averageCurrentXLessStreak + "/" + maxCurrentXLessStreak;
    maxXLessStreakStats.innerHTML = minMaxXLessStreak + "/" + averageMaxXLessStreak + "/" + maxMaxXLessStreak;
    currentPostStreakStats.innerHTML = minCurrentPostStreak + "/" + averageCurrentPostStreak + "/" + maxCurrentPostStreak;
    maxPostStreakStats.innerHTML = minMaxPostStreak + "/" + averageMaxPostStreak + "/" + maxMaxPostStreak;
    currentCombinedStreakStats.innerHTML = minCurrentCombinedStreak + "/" + averageCurrentCombinedStreak + "/" + maxCurrentCombinedStreak;
    maxCombinedStreakStats.innerHTML = minMaxCombinedStreak + "/" + averageMaxCombinedStreak + "/" + maxMaxCombinedStreak;

    n.innerHTML = wordleStats['n'];
    score.innerHTML = wordleStats['score'];
    offByOneCount.innerHTML = wordleStats['offByOneCount'];
    offByOneAverage.innerHTML = wordleStats['offByOneAverage'] + '%';

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
    result1Average.innerHTML = wordleStats['result1Average'] + '%';
    result2Count.innerHTML = wordleStats['result2Count'];
    result2Average.innerHTML = wordleStats['result2Average'] + '%';
    result3Count.innerHTML = wordleStats['result3Count'];
    result3Average.innerHTML = wordleStats['result3Average'] + '%';
    result4Count.innerHTML = wordleStats['result4Count'];
    result4Average.innerHTML = wordleStats['result4Average'] + '%';
    result5Count.innerHTML = wordleStats['result5Count'];
    result5Average.innerHTML = wordleStats['result5Average'] + '%';
    result6Count.innerHTML = wordleStats['result6Count'];
    result6Average.innerHTML = wordleStats['result6Average'] + '%';
    resultXCount.innerHTML = wordleStats['resultXCount'];
    resultXAverage.innerHTML = wordleStats['resultXAverage'] + '%';

    currentXLessStreak.innerHTML = wordleStats['currentXLessStreak'];
    maxXLessStreak.innerHTML = wordleStats['maxXLessStreak'];
    currentPostStreak.innerHTML = wordleStats['currentPostStreak'];
    maxPostStreak.innerHTML = wordleStats['maxPostStreak'];
    currentCombinedStreak.innerHTML = wordleStats['currentCombinedStreak'];
    maxCombinedStreak.innerHTML = wordleStats['maxCombinedStreak'];
}