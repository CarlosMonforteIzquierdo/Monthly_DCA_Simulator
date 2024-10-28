// `dates`, `portfolioValues`, `investedAmounts`, y `ticker` deben ser pasadas desde el HTML
const ctx = document.getElementById('investmentChart').getContext('2d');
const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: dates,  // X-axis (Dates)
        datasets: [
            {
                label: 'Portfolio Value',
                data: portfolioValues,  // Y-axis (Portfolio Value)
                borderColor: 'rgb(255, 166, 43)',
                fill: false
            },
            {
                label: 'Invested Amount',
                data: investedAmounts,  // Y-axis (Invested Amount)
                borderColor: 'rgb(72, 159, 181)',
                fill: false
            }
        ]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: `Dollar Cost Averaging for ${ticker}`
            }
        }
    }
});
