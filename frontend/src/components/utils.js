const date = new Date();
const months = Array.from({ length: 12 }, (_, i) => {
  date.setMonth(i);
  return date.toLocaleString("default", { month: "long" });
});

export const options = {
  plugins: {
    zoom: {
      pan: {
        enabled: true,
        mode: "x",
        speed: 0.1,
      },
      zoom: {
        wheel: {
          enabled: true,
          speed: 0.000000001,
        },
        pinch: {
          enabled: true,
        },
        mode: "x",
      },
    },
  },
  scales: {
    x: {
      border: {
        color: "rgb(238, 236, 236)",
        dash: [4, 4],
      },
      ticks: {
        color: "#a3aeb9",
        backdropColor: "yallow",
        textStrokeColor: "blue",
      },
      grid: {
        display: true,
        color: "rgb(238, 236, 236)",
        tickColor: "rgb(238, 236, 236)",
      },
    },
    y: {
      grace: 1,
      ticks: {
        color: "#a3aeb9",
        backdropColor: "yallow",
        textStrokeColor: "blue",
        callback: function (value, index, values) {
          // Check if it is the last tick
          if (index === values.length - 1) {
            return null; // Do not display the last tick
          }
          return value; // Display other ticks
        },
      },

      border: {
        color: "rgb(238, 236, 236)",
        dash: [4, 4],
      },
      grid: {
        drawTicks: false,
        color: "rgb(238, 236, 236)",
      },
    },
  },
};

export const data = {
  labels: [],
  datasets: [
    {
      label: "Bar Dataset",
      data: [],
      backgroundColor: "rgba(25,119,242,255)",
      borderColor: "rgba(25,119,242,255)",
      borderRadius: 10,
      borderWidth: 1,
      type: "bar",
    },
    {
      label: "Bar Dataset",
      data: [],
      backgroundColor: "#ffc143",
      borderColor: "#ffc143",
      borderRadius: 10,
      borderWidth: 1,
      type: "bar",
    },
    {
      label: "Bar Dataset",
      data: [],
      backgroundColor: "#5fd3e7",
      borderColor: "#5fd3e7",
      borderRadius: 10,
      borderWidth: 1,
      type: "bar",
    },
    {
      label: "Line Dataset",
      data: [],
      fill: false,
      borderColor: "#5fd3e7",
      borderRadius: 10,
      type: "line",
    },
  ],
};
export const processDatabaseData = (databaseData) => {
  const labels = months;
  const revenueList = databaseData["Revenue"];
  const expensesList = databaseData["Expenses"];
  const profitList = databaseData["Profit"];

  return {
    labels: labels,
    datasets: [
      {
        label: "Revenue",
        data: revenueList,
        backgroundColor: "rgba(25,119,242,255)",
        borderColor: "rgba(25,119,242,255)",
        borderRadius: 10,
        borderWidth: 1,
        type: "bar",
      },
      {
        label: "Expenses",
        data: expensesList,
        backgroundColor: "#ffc143",
        borderColor: "#ffc143",
        borderRadius: 10,
        borderWidth: 1,
        type: "bar",
      },

      {
        label: "profit",
        data: profitList,
        fill: false,
        borderColor: "#5fd3e7",
        borderRadius: 10,
        type: "line",
      },
    ],
  };
};
export const defaultDataSets = () => {
  return {
    labels: [],
    datasets: [
      {
        label: "Bar Dataset",
        data: [],
        backgroundColor: "rgba(25,119,242,255)",
        borderColor: "rgba(25,119,242,255)",
        borderRadius: 10,
        borderWidth: 1,
        type: "bar",
      },
      {
        label: "Bar Dataset",
        data: [],
        backgroundColor: "#ffc143",
        borderColor: "#ffc143",
        borderRadius: 10,
        borderWidth: 1,
        type: "bar",
      },
      {
        label: "Bar Dataset",
        data: [],
        backgroundColor: "#5fd3e7",
        borderColor: "#5fd3e7",
        borderRadius: 10,
        borderWidth: 1,
        type: "bar",
      },
      {
        label: "Line Dataset",
        data: [],
        fill: false,
        borderColor: "#5fd3e7",
        borderRadius: 10,
        type: "line",
      },
    ],
  };
};
