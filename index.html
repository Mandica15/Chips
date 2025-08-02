<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Rentz Scoreboard</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f8f8f8;
      padding: 20px;
    }

    h1 {
      text-align: center;
      margin-bottom: 20px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      background: white;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    th, td {
      border: 1px solid #ccc;
      padding: 10px;
      text-align: center;
    }

    th {
      background: #4CAF50;
      color: white;
      position: sticky;
      top: 0;
      z-index: 1;
    }

    tr:nth-child(even) {
      background: #f2f2f2;
    }

    input[type="number"] {
      width: 60px;
      padding: 5px;
      text-align: center;
      border: 1px solid #aaa;
      border-radius: 4px;
    }

    .totals-row {
      font-weight: bold;
      background: #ddd;
    }

    button {
      margin-top: 10px;
      padding: 10px 20px;
      background: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
      border-radius: 5px;
    }

    button:hover {
      background: #45a049;
    }
  </style>
</head>
<body>

<h1>Rentz - Tabel de scor</h1>

<table id="scoreboard">
  <thead>
    <tr>
      <th>Rundă</th>
      <th>Joc</th>
      <th>Jucător 1</th>
      <th>Jucător 2</th>
      <th>Jucător 3</th>
      <th>Jucător 4</th>
    </tr>
  </thead>
  <tbody id="scoreRows">
    <!-- Example row -->
    <tr>
      <td>1</td>
      <td>
        <select>
          <option>Rentz</option>
          <option>Dame</option>
          <option>Popa de Pică</option>
          <option>Zece de Cupă</option>
          <option>Ultima Carte</option>
          <option>Fără Ultima Carte</option>
          <option>Fără Cărți</option>
          <option>Fără Inimă Roșie</option>
          <option>Fără Niciuna</option>
          <option>Table</option>
        </select>
      </td>
      <td><input type="number" value="0" onchange="updateTotals()" /></td>
      <td><input type="number" value="0" onchange="updateTotals()" /></td>
      <td><input type="number" value="0" onchange="updateTotals()" /></td>
      <td><input type="number" value="0" onchange="updateTotals()" /></td>
    </tr>
  </tbody>
  <tfoot>
    <tr class="totals-row">
      <td colspan="2">Total</td>
      <td id="total1">0</td>
      <td id="total2">0</td>
      <td id="total3">0</td>
      <td id="total4">0</td>
    </tr>
  </tfoot>
</table>

<button onclick="addRow()">Adaugă rundă</button>

<script>
  function addRow() {
    const table = document.getElementById("scoreRows");
    const rowCount = table.rows.length + 1;
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${rowCount}</td>
      <td>
        <select>
          <option>Rentz</option>
          <option>Dame</option>
          <option>Popa de Pică</option>
          <option>Zece de Cupă</option>
          <option>Ultima Carte</option>
          <option>Fără Ultima Carte</option>
          <option>Fără Cărți</option>
          <option>Fără Inimă Roșie</option>
          <option>Fără Niciuna</option>
          <option>Table</option>
        </select>
      </td>
      <td><input type="number" value="0" onchange="updateTotals()" /></td>
      <td><input type="number" value="0" onchange="updateTotals()" /></td>
      <td><input type="number" value="0" onchange="updateTotals()" /></td>
      <td><input type="number" value="0" onchange="updateTotals()" /></td>
    `;
    table.appendChild(row);
  }

  function updateTotals() {
    const totals = [0, 0, 0, 0];
    const rows = document.querySelectorAll("#scoreRows tr");
    rows.forEach(row => {
      row.querySelectorAll("input[type='number']").forEach((input, index) => {
        totals[index] += parseInt(input.value) || 0;
      });
    });
    totals.forEach((total, index) => {
      document.getElementById(`total${index + 1}`).innerText = total;
    });
  }

  // Initialize with totals
  updateTotals();
</script>

</body>
</html>
