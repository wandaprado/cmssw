import FWCore.ParameterSet.Config as cms

RungeKuttaTrackerPropagatorOpposite = cms.ESProducer("PropagatorWithMaterialESProducer",
    MaxDPhi = cms.double(1.6),
    ComponentName = cms.string('RungeKuttaTrackerPropagatorOpposite'),
    Mass = cms.double(0.105),
    PropagationDirection = cms.string('oppositeToMomentum'),
    useRungeKutta = cms.bool(True),
# If ptMin > 0, uncertainty in reconstructed momentum will be taken into account when estimating rms scattering angle.
# (By default, it is neglected). However, it will also be assumed that the track pt can't be below specified value,
# to prevent this scattering angle becoming too big.                                    
    ptMin = cms.double(-1.)
)



