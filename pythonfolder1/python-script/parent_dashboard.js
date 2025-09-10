// Initialize FullCalendar on the dashboard

document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        height: 400,
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        events: [
            // Example events
            { title: 'Family Meeting', start: new Date().toISOString().slice(0,10) },
            { title: 'Reward: Ice Cream', start: new Date(Date.now() + 86400000).toISOString().slice(0,10) }
        ]
    });
    calendar.render();
});
