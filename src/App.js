import React from 'react';
import Layout from './components/Layout';

class App extends React.Component {
  render() {
    return (
        <div className="App">
          <Layout deps={["Department 1", "Department 2"]} title={"Question Paper Generator"}/>
        </div>
    );
  }
}

export default App;
