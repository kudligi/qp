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

  getPaperList() {
    fetch('http://127.0.0.1:5000/metadata/course_list')
      .then(response => response.json())
      .then(courses =>
            this.setState({courses: courses})
           );
  }

    render() {
        const courses = [
            {
                name: "Course 1",
                deps: [
                    {
                        name: "Dep 1",
                        papers: ["Paper 1", "Paper 2", "Paper 3"]
                    },
                    {
                        name: "Dep 2",
                        papers: ["Paper 1", "Paper 2"]
                    }
                ]
            },
            {
                name: "Course 2",
                deps: [
                    {
                        name: "Dep 1",
                        papers: ["Paper 1", "Paper 2", "Paper 3"]
                    },
                    {
                        name: "Dep 2",
                        papers: ["Paper 1", "Paper 2"]
                    },
                    {
                        name: "Dep 3",
                        papers: ["Paper 1", "Paper 2", "Paper 3"]
                    }

                ]
            },
            {
                name: "Course 3",
                deps: [
                    {
                        name: "Dep 1",
                        papers: ["Paper 1", "Paper 2", "Paper 3"]
                    },
                    {
                        name: "Dep 2",
                        papers: ["Paper 1", "Paper 2"]
                    }

                ]
            }
        ];
        const title = "Question Paper Generator";
        this.getPaperList();
        return (
            <div className="App">
              <Layout courses={courses} title={title} />
            </div>
        );
    }
}

export default App;
