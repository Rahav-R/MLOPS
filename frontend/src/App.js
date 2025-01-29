import React, { Component } from "react";
import axios from "axios";

class App extends Component {
  state = {
    value1: "",
    value2: "",
    value3: "",
    value4: "",
    value5: "",
    value6: "",
    value7: "",
    value8: "",
    prediction: null,
    error: null,
  };

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  };

  handleSubmit = async (e) => {
    e.preventDefault();
    const { value1, value2, value3, value4, value5, value6, value7, value8 } = this.state;

    // Validate input values (basic validation for numbers)
    if (
      ![value1, value2, value3, value4, value5, value6, value7, value8].every((val) =>
        /^[0-9.]+$/.test(val)
      )
    ) {
      this.setState({ error: "Please ensure all fields contain valid numeric values." });
      return;
    }

    try {
      const response = await axios.post("http://localhost:8000", {
        v1: value1,
        v2: value2,
        v3: value3,
        v4: value4,
        v5: value5,
        v6: value6,
        v7: value7,
        v8: value8,
      });

      this.setState({ prediction: response.data.prediction, error: null });
    } catch (err) {
      this.setState({
        error: "Failed to fetch prediction. Please check your backend or try again later.",
      });
    }
  };

  render() {
    const { value1, value2, value3, value4, value5, value6, value7, value8, prediction, error } =
      this.state;

    return (
      <div style={{ fontFamily: "Arial, sans-serif", padding: "20px", backgroundColor: "#333" }}>
        <h1 style={{ color: "wheat" }}>Heart Disease Predictor</h1>
        <form onSubmit={this.handleSubmit} style={{ maxWidth: "400px", margin: "0 auto" }}>
          {["Age", "Gender", "Heart-rate", "Systolic blood pressure", "Diastolic blood pressure", "Blood Sugar", "CKMB", "Troponin"].map(
            (label, index) => (
              <div key={index} style={{ marginBottom: "10px" }}>
                <label
                  htmlFor={`value${index + 1}`}
                  style={{ display: "block", color: "wheat", marginBottom: "5px" }}
                >
                  {label}:
                </label>
                <input
                  type="text"
                  id={`value${index + 1}`}
                  name={`value${index + 1}`}
                  value={this.state[`value${index + 1}`]}
                  onChange={this.handleChange}
                  style={{
                    width: "100%",
                    padding: "8px",
                    border: "1px solid #ccc",
                    borderRadius: "4px",
                  }}
                />
              </div>
            )
          )}
          <button
            type="submit"
            style={{
              display: "block",
              width: "100%",
              padding: "10px",
              backgroundColor: "#4CAF50",
              color: "white",
              border: "none",
              borderRadius: "4px",
              cursor: "pointer",
            }}
          >
            Submit
          </button>
        </form>
        {prediction !== null && (
          <div style={{ marginTop: "20px", color: "wheat" }}>
            <h2>Prediction:</h2>
            <p>{prediction}</p>
          </div>
        )}
        {error && (
          <div
            style={{
              marginTop: "20px",
              color: "#FF3333",
              backgroundColor: "#FFF3F3",
              padding: "10px",
              border: "1px solid #FF3333",
              borderRadius: "4px",
            }}
          >
            {error}
          </div>
        )}
      </div>
    );
  }
}

export default App;
