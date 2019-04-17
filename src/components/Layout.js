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

const drawerWidth = 240;

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
            table: "",
            selected: false,
        };

        this.handleSelect = this.handleSelect.bind(this);
    }

    handleSelect(select) {
        this.setState(state => ({table: select, selected: true}));
    }

    render() {
        let rows = [
            {id: 0, name: "Cupcake", calories: 305, fat: 3.7},
            {id: 1, name: "Donut", calories: 452, fat: 25.0},
            {id: 2, name: "Eclair", calories: 262, fat: 16.0},
            {id: 3, name: "Frozen yoghurt", calories: 159, fat: 6.0},
            {id: 4, name: "Gingerbread", calories: 356, fat: 16.0},
            {id: 5, name: "Honeycombe", calories: 408, fat: 3.2},
            {id: 6, name: "KitKat", calories: 518, fat: 26.0},
            {id: 7, name: "Oreo", calories: 437, fat: 18.0},
        ];
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
                  {this.props.deps.map((text, index) => (
                      <DropDown head={text} list={this.props.subs} key={index} handleSelect={this.handleSelect}></DropDown>
                  ))}
                </List>
              </Drawer>
              <main className={classes.content}>
                <div className={classes.toolbar} />
                {this.state.selected && <DataTable rows={rows} />}
              </main>
            </div>
        );
    }
}

export default withStyles(styles)(Layout);
