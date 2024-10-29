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
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display:true,
                position: 'top',
            },
            title: {
                display: true,
                text: `Dollar Cost Averaging for ${ticker}`
            }
        }
    }
});

let resizeTimeout;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
        myChart.resize(); // Ajusta el gráfico al nuevo tamaño
    }, 100); // Ajuste de 200ms
});
