document.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed');

    const multiSelects = document.querySelectorAll('.select-multiple');

    multiSelects.forEach(select => {
        console.log('Found select element:', select);

        select.addEventListener('mousedown', function(e) {
            if (e.target.tagName === 'OPTION') {
                console.log('Option clicked:', e.target);
                e.preventDefault(); // Prevent the default action

                if (e.target.selected) {
                    e.target.selected = false;
                } else {
                    e.target.selected = true;
                }

                const changeEvent = new Event('change', { bubbles: true });
                select.dispatchEvent(changeEvent);
            }
        });
    });
});
