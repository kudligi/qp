import React from 'react';
import Layout from './components/Layout';

class App extends React.Component {
    render() {
        const deps = ["Department 1: Paper 1", "Department 1: Paper 2", "Department 2: Paper 1"];
        const title = "Question Paper Generator";
        const subs = ["Breakup", "Legend", "Question Bank"];
        return (
        <div className="App">
          <Layout deps={deps} title={title} subs={subs}/>
        </div>
    );
  }
}

export default App;
