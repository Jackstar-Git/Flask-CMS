const chart = window.chart


const userChart = document.getElementById("user-chart")
const postsChart = document.getElementById("post-chart")
const commentChart = document.getElementById("comment-chart")


const userData = {
    labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    datasets: [{
        label: 'Total Users',
        data: [726, 1342, 657, 1024, 389, 1307, 1234],
        borderColor: "#FF0000CC",
        pointRadius: 5,
        pointBackgroundColor: "#FF0000CC"},
        {
        label: "Active Users",
        data: [512, 142, 735, 290, 678, 128, 789],
        borderColor: "#00FF00CC",
        pointRadius: 5,
        pointBackgroundColor: "#00FF00CC"},
        {
        label: 'New Signups',
        data: [23, 67, 12, 89, 5, 34, 45],
        borderColor: "#0000FFCC",
        pointRadius: 5,
        pointBackgroundColor: "#0000FFCC"}
    ]};


new Chart(userChart, {
    type: 'line',
    data: userData,
    options: {
        maintainAspectRatio: false,
        responsive: true,
        scales: {
            y: {
                grace: "10%",
                min: 0
            }
        }
},})

const postData = {
    labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    datasets: [{
        label: 'Total Posts',
        data: [450, 523, 499, 401, 589, 520, 567],
        borderColor: "#FF5733CC",
        pointRadius: 5,
        pointBackgroundColor: "#FF5733CC"},
        {
        label: "Published Posts",
        data: [420, 456, 485, 404, 472, 434, 432]   ,
        borderColor: "#28A745CC",
        pointRadius: 5,
        pointBackgroundColor: "#28A745CC"},
        {
        label: 'Draft Posts',
        data: [112, 137, 140, 103, 144, 129, 135],
        borderColor: "#1E90FFCC",
        pointRadius: 5,
        pointBackgroundColor: "#1E90FFCC"}
    ]};


new Chart(postsChart, {
    type: 'line',
    data: postData,
    options: {
        maintainAspectRatio: false,
        responsive: true,
        scales: {
            y: {
                grace: "10%",
                min: 0
            }
        }
},})

const commentData = {
    labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    datasets: [{
        label: 'Total Comments',
        data: [2354, 2187, 2441, 2059, 2222, 2403, 2456],
        borderColor: "#00CED1CC ",
        pointRadius: 5,
        pointBackgroundColor: "#00CED1CC"},
        {
        label: "Approved Comments",
        data: [1915, 1948, 1964, 1921, 1995, 1987, 1980],
        borderColor: "#FFD700CC",
        pointRadius: 5,
        pointBackgroundColor: "#FFD700CC"},
        {
        label: 'Pending Comments',
        data: [445, 476, 417, 469, 487, 405, 476],
        borderColor: "#DC1431CC",
        pointRadius: 5,
        pointBackgroundColor: "#DC1431CC"}
    ]};


new Chart(commentChart, {
    type: 'line',
    data: commentData,
    options: {
        maintainAspectRatio: false,
        responsive: true,
        scales: {
            y: {
                grace: "10%",
                min: 0
            }
        }
},})

