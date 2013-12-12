/* Insert default data to data base */

USE watchtips;

INSERT INTO wt_user
(user_id, user_name, user_password)
VALUES
(1, 'god', 'odg');

INSERT INTO wt_category
(category_id, category_name, user_id)
VALUES
(1, 'default', 1),
(2, 'python', 1),
(3, 'javascript', 1),
(4, 'html5', 1);

INSERT INTO wt_tips
(tips_id, tips_title, tips_content, category_id)
VALUES
(1, '', 'Add your tips', 1),
(2, '', 'Watch your tips', 1),
(3, '', 'Forget your tips', 1);
