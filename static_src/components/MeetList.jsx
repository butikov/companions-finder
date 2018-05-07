import React from 'react';
import PropTypes from 'prop-types';

import Meet from './Meet'

class MeetList extends React.Component{
    static propTypes = {
        isLoading: PropTypes.bool,
        meetList: PropTypes.arrayOf(PropTypes.shape(Meet.propTypes)),
    };

    static contextTypes = {
        store: PropTypes.object,
    };

    static defaultProps = {
        meetList: [],
        isLoading: false,
    };

    render() {
        if (this.props.isLoading) {
            return <div className='b-meet-list'>Loading...</div>
        }
        const meets = this.props.meetList.map(
            item => <Meet key={ item.id} author={ item.author} title={item.title} text={item.text}/>,
        );
        return (
          <div className='b-meet-list'>
              {meets}
          </div>
        );
    }
}

export default MeetList;