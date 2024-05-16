const ride = new Promise((res, rej) => {
    if (arrived) {
        console.log('Driver arrived');
    } else {
        console.log('Driver bailed');
    }
});

ride
    .then()
    .catch();
