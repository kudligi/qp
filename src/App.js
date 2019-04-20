import React from 'react';
import Layout from './components/Layout';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      courses: [],
      deps: [],
      papers: []
    };
  }

  getCourses() {
    fetch('http://127.0.0.1:5000/metadata/all_papers')
      .then(response => response.json())
      .then(courses =>
            this.setState({courses: courses})
           );
  }

  componentDidMount() {
    this.getCourses();
  }

  render() {
      const title = "Question Paper Generator";
      return (
        <div className="App">
          <Layout courses={this.state.courses} title={title} />
        </div>
      );
    }
}

export default App;
