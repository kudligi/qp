import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import CssBaseline from '@material-ui/core/CssBaseline';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import DropDown from './Dropdown';
import DataTable from './Table';

const drawerWidth = 300;

const styles = theme => ({
  root: {
    display: 'flex',
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0,
  },
  drawerPaper: {
    width: drawerWidth,
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing.unit * 3,
  },
  toolbar: theme.mixins.toolbar,
});

class Layout extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [{
        firstName: "Anirudh",
        lastName: "C",
        username: "anirudh-c",
        email: "anirudh.c@iiitb.org"
      }],
      header: [
        {
          name: "First name",
          prop: "firstName"
        },
        {
          name: "Last name",
          prop: "lastName"
        },
        {
          name: "Username",
          prop: "username"
        },
        {
          name: "Email",
          prop: "email"
        }
      ],
      table: "",
      selected: false,
      editIdx: -1
    };

    this.handleRemove = this.handleRemove.bind(this);
    this.startEditing = this.startEditing.bind(this);
    this.stopEditing = this.stopEditing.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.handleSelect = this.handleSelect.bind(this);
  }

  handleRemove(i) {
    this.setState(state => ({
      data: state.data.filter((row, j) => j !== i)
    }));
  }

  startEditing(i) {
    this.setState({ editIdx: i });
  }

  stopEditing() {
    this.setState({ editIdx: -1 });
  }

  handleChange(e, name, i) {
    const { value } = e.target;
    this.setState(state => ({
      data: state.data.map(
        (row, j) => (j === i ? { ...row, [name]: value } : row)
      )
    }));
  }

  handleSelect(select) {
    this.setState(state => ({table: select, selected: true}));
  }

  render() {
    const { classes } = this.props;

    return (
      <div className={classes.root}>
        <CssBaseline />
        <AppBar position="fixed" className={classes.appBar}>
          <Toolbar>
            <Typography variant="h6" color="inherit" noWrap>
              {this.props.title}
            </Typography>
          </Toolbar>
        </AppBar>
        <Drawer className={classes.drawer} variant="permanent" classes={{ paper: classes.drawerPaper, }}>
          <div className={classes.toolbar} />
          <List>
            {this.props.courses.map((course, index) => (
                <DropDown course={course} key={index} handleSelect={this.handleSelect}></DropDown>
            ))}
          </List>
        </Drawer>
        <main className={classes.content}>
          <div className={classes.toolbar} />
          <DataTable
            handleRemove={this.handleRemove}
            startEditing={this.startEditing}
            editIdx={this.state.editIdx}
            stopEditing={this.stopEditing}
            handleChange={this.handleChange}
            data={this.state.data}
            header={this.state.header}
          />
        </main>
      </div>
    );
  }
}

export default withStyles(styles)(Layout);
