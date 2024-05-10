Embedding js in pelican
#########################

:date: 2024-01-22
:tags: pelican, javascript
:authors: Matt Gibson
:modified: 2024-04-04


.. raw:: HTML

    <img src="{static}/images/pious_pelican.png" alt="The pelican "></img>


Sometimes I like to  write a little js in my blog posts. Here is an example of how to embed a javascript file in a pelican article.

.. raw:: html

    <div id="demo"></div>
    <script src="{static}/js/demo.js"></script>

Below the fold, is an example of embedding a js chart into a pelican article. Specifically, we have the crude marriage rates in Australia for 2000 to 2022. Not many surprises here, the crude marriage rate has been in decline for the past 20 years, barring some minor fluctions most dramatically due to Covid.

.. raw:: html

    <div>
    <canvas id="myChart"></canvas>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <script>
    const ctx = document.getElementById('myChart');

    new Chart(ctx, {
        type: 'line',
        data: {
        labels: ['2020',	'2019',	'2018','2017',	'2016',	'2015',	'2014',	'2013',	'2012',	'2011',	'2010',	'2009',	'2008',	'2007',	'2006',	'2005',	'2004',	'2003',	'2002',	'2001',	'2000'].toReversed(),
        datasets: [{
            label: 'marriages per 1,000 residents in Australia',
            data: [3.1, 4.5, 4.8, 4.6, 4.9, 4.8, 5.2, 5.1, 5.4, 5.4, 5.4, 5.5, 5.5, 5.5, 5.5, 5.4, 5.5, 5.4, 5.4, 5.3, 5.9].toReversed(),
            borderWidth: 1
        }]
        },
        options: {
        scales: {
            y: {
            beginAtZero: true
            }
        },
            animation: {
        duration: 0
    }
        }
    });
    </script>

source data: `Parliamentary library <https://www.aph.gov.au/About_Parliament/Parliamentary_Departments/Parliamentary_Library/FlagPost/2021/December/Marriage_and_divorce>`_

Note `this website <https://www.statista.com/statistics/610957/australia-crude-marriage-rate/>`_ here is wrong because the `ABS changed there methods <https://www.abs.gov.au/statistics/people/people-and-communities/marriages-and-divorces-australia/latest-release#marriages>`_. Pretty cheeky to charge you $199 USD per year for bad collation of public data. 