import React from 'react';
import PropTypes from 'prop-types';

import User from './User'

class Meet extends React.Component {
    static propTypes = {
        id: PropTypes.number,
        title: PropTypes.string,
        text: PropTypes.string,
        author: PropTypes.shape(User.propTypes).isRequired,
        meet_time: PropTypes.string,
        participants: PropTypes.array,
        max_participants: PropTypes.number,
    };

    static defaultProps = {
        text: '',
    };

    render() {
        return (
            <div className='b-meet'>
                <User
                    id={this.props.author.id}
                    avatar={this.props.author.avatar}
                    first_name={this.props.author.first_name}
                />
                <div className='b-meet-title'>
                    <div className='b-user-name'>{this.props.title}</div>
                </div>
                <div className='b-meet-content'>{ this.props.text }</div>
            </div>
        );
    }
}

export default  Meet;
