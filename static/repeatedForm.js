const mainSel = document.querySelector("#period");
const subLabel = document.querySelector("#sub-label")
const subInput = document.querySelector("#sub-input")

function periodChange() {
  const dateArr = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday',];
  const monthArr = [];

  for(let i=1; i<=31; i++) {
    monthArr.push(i);
  }

  //Sub-selection content
  function subSel(arr) {
    let result = "";
    arr.forEach(i => {
      if(typeof i === "number") {
        result += `<option value=${i}>${i}</option>`;
      }
      if(typeof i === "string") {
        result += `<option value=${i.toLowerCase()}>${i}</option>`;
      } 
    })
    return result;
  }

  //Add label content once period being clicked
  switch (mainSel.value) {
    case "e-year":
      subLabel.innerHTML = `
      Choose Specific Date of A Year: 
      <input name="sub-input" id="sub-input" type="date" />
      `;
      break;
    case "e-month":
      subLabel.innerHTML = `
      Choose Specific Date of A Month: 
      <select name="date" id="date">
        ${subSel(monthArr)}
      </select>
      `;
      break;
    case "e-week":
    case "e-fortnight":
      subLabel.innerHTML = `
      Choose Specific Date of A Week: 
      <select name="date" id="date">
        ${subSel(dateArr)}
      </select>
      `;
      break;
    default:
      subLabel.innerHTML = '';
  }
}