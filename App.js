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

  handleSubmit = (e) => {
    e.preventDefault();
    const { value1, value2, value3, value4, value5,value6,value7,value8 } = this.state;

    axios.post("http://127.0.0.1:8000", {
        v1: value1,
        v2: value2,
        v3: value3,
        v4: value4,
        v5: value5,
        v6: value6,
        v7: value7,
        v8: value8,
      })
      .then((response) => {
        this.setState({ prediction: response.data.prediction, error: null });
      })
      
  };
  

  render() {
    const { value1, value2, value3, value4, value5,value6,value7,value8, prediction, error } = this.state;

    return (
      <div>
        <h1 style={{ paddingLeft: '10px', color:'wheat' }}>Heart Disease Predictor</h1>
        <form onSubmit={this.handleSubmit}>
          <div style={{ marginBottom: '10px'}}>
            <label style={{ marginRight: '10px' , marginLeft:'20px', color:'wheat' }}>Age:</label>
            <input type="text" name="value1" value={value1} onChange={this.handleChange} />
          </div>
          <div style={{ marginBottom: '10px' }}>
            <label style={{ marginRight: '10px' , marginLeft:'20px', color:'wheat' }}>Gender:</label>
            <input type="text" name="value2" value={value2} onChange={this.handleChange} />
          </div>
          <div style={{ marginBottom: '10px' }}>
            <label style={{ marginRight: '10px' , marginLeft:'20px', color:'wheat' }}>Heart-rate:</label>
            <input type="text" name="value3" value={value3} onChange={this.handleChange} />
          </div>
          <div style={{ marginBottom: '10px' }}>
            <label style={{ marginRight: '10px' , marginLeft:'20px', color:'wheat' }}>Systolic blood pressure:</label>
            <input type="text" name="value4" value={value4} onChange={this.handleChange} />
          </div>
          <div style={{ marginBottom: '10px' }}>
            <label style={{ marginRight: '10px' , marginLeft:'20px', color:'wheat' }}>Distolic blood pressure:</label>
            <input type="text" name="value5" value={value5} onChange={this.handleChange} />
          </div>
          <div style={{ marginBottom: '10px' }}>
            <label style={{ marginRight: '10px' , marginLeft:'20px', color:'wheat' }}>Blood Sugar:</label>
            <input type="text" name="value6" value={value6} onChange={this.handleChange} />
          </div>
          <div style={{ marginBottom: '10px' }}>
            <label style={{ marginRight: '10px' , marginLeft:'20px', color:'wheat' }}>CKMB:</label>
            <input type="text" name="value7" value={value7} onChange={this.handleChange} />
          </div>
          <div style={{ marginBottom: '10px' }}>
            <label style={{ marginRight: '10px' , marginLeft:'20px', color:'wheat' }}>Troponin:</label>
            <input type="text" name="value8" value={value8} onChange={this.handleChange} />
          </div>
          <div style={{ marginRight: '10px' , marginLeft:'20px', color:'wheat'}}>
          <button type="submit">Submit</button>
          </div>
        </form>
        {prediction !== null && (
          <div>
            <h2 style={{ marginRight: '10px' , marginLeft:'20px', color:'wheat'}}>Prediction:</h2>
            <p style={{ marginRight: '10px' , marginLeft:'20px', color:'wheat'}}>{prediction}</p>
          </div>
        )}
        {error && <div>Error: {error}</div>}
      </div>
    );
  }
}

export default App;