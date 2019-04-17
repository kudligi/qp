import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import CssBaseline from '@material-ui/core/CssBaseline';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import DropDown from './Dropdown';

const drawerWidth = 360;

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
            selected: "",
        };

        this.handleSelect = this.handleSelect.bind(this);
    }

    handleSelect(select) {
        this.setState(state => ({selected: select}));
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
                  {this.props.deps.map((text, index) => (
                      <DropDown head={text} list={this.props.subs} key={index} handleSelect={this.handleSelect}></DropDown>
                  ))}
                </List>
              </Drawer>
              <main className={classes.content}>
                <div className={classes.toolbar} />
              </main>
            </div>
        );
    }
}

export default withStyles(styles)(Layout);
