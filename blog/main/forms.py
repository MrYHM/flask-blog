from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, PasswordField, ValidationError,TextAreaField
from wtforms.validators import Required, Length, Email, EqualTo, Regexp
from ..models import User
from flask_login import current_user
from flask_uploads import UploadSet, IMAGES


images = UploadSet('images', IMAGES)


class UserInfo(FlaskForm):
    realname = StringField('真实姓名', validators=[Length(1, 64)])
    location = StringField('居住地', validators=[Length(1, 64)])
    abortme = TextAreaField('个人介绍', validators=[Length(1, 64)])
    submit = SubmitField('提交')


class UserPasswd(FlaskForm):
    oldpassword = PasswordField('旧的密码', validators=[Required()])
    newpassword = PasswordField(
        '新的密码', validators=[Required(), EqualTo('newpassword2', message=u'密码不一致')])
    newpassword2 = PasswordField('确认新密码', validators=[Required()])
    submit = SubmitField('提交')

    def validate_oldpassword(self, field):
        if not current_user.verify_password(field.data):
            raise ValidationError('密码输入有误')


class Avatar(FlaskForm):
    avatar = FileField('上传头像', validators=[
                       FileRequired(), FileAllowed(['jpg', 'png'], '只能上传图片')])
    submit = SubmitField('提交')

class TopicForm(FlaskForm):
    topic_name = StringField('话题名',validators=[Required(),Length(1,64)])
    topic_info = TextAreaField('话题描述')
    topic_img = FileField('话题图片',validators=[FileRequired(),FileAllowed(['jpg','png'],'只能上传图片')])
    submit = SubmitField('提交')