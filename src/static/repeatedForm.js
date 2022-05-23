const mainSel = document.querySelector("#period");
const subInput = document.querySelector("#sub-input");
const submitBtn = document.querySelector(".submitBtn");
const form = document.querySelector("form");



function periodChange() {
  const dateArr = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
  ];
  const monthArr = [];

  for (let i = 1; i <= 31; i++) {
    monthArr.push(i);
  }

  //Sub-selection content
  function subSel(arr) {
    let result = "";
    arr.forEach((i) => {
      if (typeof i === "number") {
        result += `<option value=${i}>${i}</option>`;
      }
      if (typeof i === "string") {
        result += `<option value=${i.toLowerCase()}>${i}</option>`;
      }
    });
    return result;
  }

  //To remove prev existing sub selection
  function removePrevSubSel() {
    let subSelection = document.querySelector(".sub-sel");
    if (subSelection) {
      subSelection.remove();
      console.log('removed')
    }
  }

  //Add label content once period being clicked
  switch (mainSel.value) {
    case "e-year":
      removePrevSubSel();
      submitBtn.insertAdjacentHTML(
        "beforebegin",
        `
      <div class="sub-sel form-group mt-4">
        <label for="date">Choose Specific Date of A Year</label>         
        <input class="form-control" name="date" id="date" type="date" required/>
      </div>
      `
      );
      break;
    case "e-month":
      removePrevSubSel();
      submitBtn.insertAdjacentHTML(
        "beforebegin",
        `
      <div class="sub-sel form-group mt-4">
        <label for="date">Choose Specific Date of A Month</label>         
        <select class="form-control custom-select" name="date" id="date">
          ${subSel(monthArr)}
        </select>
      </div>
      `
      );
      break;
    case "e-week":
    case "e-fortnight":
      removePrevSubSel();
      submitBtn.insertAdjacentHTML(
        "beforebegin",
        `
      <div class="sub-sel form-group mt-4">
        <label for="date">Choose Specific Date of A Week</label>         
        <select class="form-control custom-select" name="date" id="date">
          ${subSel(dateArr)}
        </select>
      </div>
      `
      );
      break;
    default:
      removePrevSubSel();
  }
}
