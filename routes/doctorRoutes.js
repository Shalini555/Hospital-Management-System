const express = require('express');
const router = express.Router();


const { saveDoctor,getAllDoctors,getSingleDoctor,updateDoctor,deleteDoctor } = require('../controllers/doctorController');

router.post('/addDoctor', [], saveDoctor);
router.get('/allDoctors', [],getAllDoctors);
router.get('/singleDoctors/:id', [],getSingleDoctor);
router.put('/updateDoctors/:id', [],updateDoctor);
router.delete('/deleteDoctors/:id', [],deleteDoctor);

module.exports = router;