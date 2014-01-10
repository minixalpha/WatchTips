/* Insert default data to data base */

USE watchtips;

INSERT INTO wt_user
(user_id, user_name, user_password, user_email)
VALUES
(1, 'minix', 'minix', 'minix@gmail.com');

INSERT INTO wt_category
(category_id, category_name, category_img, category_description, user_id)
VALUES
(1, 'default', 'default.png', 'Default tips', 1),
(2, 'python', 'pythonLogo.png', 'Life is short, I use python', 1),
(3, 'javascript', 'JSLogo.png', 'Not java, Not only a script', 1),
(4, 'html5', 'HTML5Logo.png', 'Language of the Web', 1);

INSERT INTO wt_tips
(tips_id, tips_title, tips_content, category_id)
VALUES
(1, '', 'Add your tips', 1),
(2, '', 'Watch your tips', 1),
(3, '', 'Forget your tips', 1);
