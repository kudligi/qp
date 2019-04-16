import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import CssBaseline from '@material-ui/core/CssBaseline';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import DropDown from './Dropdown';

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
                      <ListItem button key={text}>
                        <ListItemText primary={text} />
                      </ListItem>
                  ))}
                </List>
              </Drawer>
              <main className={classes.content}>
                <div className={classes.toolbar} />
                <DropDown list={["Item1","Item2"]}></DropDown>
              </main>
            </div>
        );
    }
}

export default withStyles(styles)(Layout);
