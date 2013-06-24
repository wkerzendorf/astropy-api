"""
The current API for models has most of the functionality we want, but, in my opinion, feels a bit clunky. I've been
working with SQLAlchemy a lot and am very happy with their API for table models.
Here's a quick Demo of one of my Table models:
"""


class GMOSMOSRawFITS(Base):
    __tablename__ = 'gmos_mos_raw_fits'

    id = Column(Integer, ForeignKey('fits_file.id'), primary_key=True)
    mjd = Column(Float)
    instrument_id = Column(Integer, ForeignKey('instrument.id'))
    observation_block_id = Column(Integer, ForeignKey('observation_block.id'))
    observation_class_id = Column(Integer, ForeignKey('observation_class.id'))
    observation_type_id = Column(Integer, ForeignKey('observation_type.id'))
    object_id = Column(Integer, ForeignKey('object.id'))
    mask_id = Column(Integer, ForeignKey('gmos_mask.id'))

# I propose an API that borrows from the Table models:

class BlackBody(modeling.Model):


    temperature = Parameter(unit='K', equivalency=None, fixed=False, tied=False, bounds=())

    frequency = ModelInput(unit='Hz', equivalency=u.spectral())
    intensity = ModelOutput(unit='erg/cm2')



mybb = BlackBody()
mybb.temperature = 10000
intensity = mybb(1 * u.angstrom)

#I feel that in this API one can immediately see from the Model definition what this models does. What it's inputs and
#outputs are. If floats are given as input, the model would convert this directly to a Quantity with the specified unit.
#If quantities are given as inputs, the model would try to convert to the specified unit.
#ModelInput and ModelOutput immediately show what's going in and out.


#For models with multiple parameters like Polynomials there's a class for Parameter sets.

class Poly1DModel(modeling.Model):

    c = ParameterSet(5, syntax='_%s', unit=None, equivalency=None, fixed=False, tied=False, bounds=())

mylittlepoly = Poly1DModel()
mylittlepoly.c_0 = 10.
mylittlepoly.fixed
False

#I'm happy to try to implement this, but would need some help with the python magic.


