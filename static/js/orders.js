document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.start-btn').forEach(btn => {
    btn.addEventListener('click', function () {
      const row = this.closest('tr');
      if (!row || row.cells.length < 9) return;

      row.classList.remove('ready');
      row.classList.add('in-progress');
      row.cells[5].textContent = 'В работе';
      row.cells[6].textContent = new Date().toLocaleTimeString();

      const doneBtn = document.createElement('button');
      doneBtn.textContent = 'ГОТОВО';
      doneBtn.classList.add('done-btn');
      doneBtn.onclick = () => {
        row.classList.remove('in-progress');
        row.classList.add('done');
        row.cells[5].textContent = 'Готово';
        row.cells[7].textContent = new Date().toLocaleTimeString();
        doneBtn.remove();
        rejectBtn.remove();
      };

      const rejectBtn = document.createElement('button');
      rejectBtn.textContent = 'БРАК';
      rejectBtn.classList.add('reject-btn');
      rejectBtn.onclick = () => {
        row.classList.remove('in-progress');
        row.classList.add('rejected');
        row.cells[5].textContent = 'Брак';
        row.cells[7].textContent = new Date().toLocaleTimeString();
        doneBtn.remove();
        rejectBtn.remove();
      };

      this.replaceWith(doneBtn);
      row.cells[8].appendChild(rejectBtn);
    });
  });

  document.querySelectorAll('.detail-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const id = btn.dataset.id;
      alert(`Карточка заказа №${id} пока не реализована`);
    });
  });
});

