package com.Hyperscale;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JComboBox;
import javax.swing.DefaultComboBoxModel;
import javax.swing.JRadioButton;
import javax.swing.JButton;
import java.awt.FlowLayout;
import java.awt.Color;

public class HyperscaleSensorTestTool extends JFrame {
	JTextArea textArea = null;
	JPanel panel_2 = null;
	JPanel panel_3 = null;
	JComboBox comboBox = null;
	JComboBox comboBox_1 = null;
	JComboBox comboBox_2 = null;
	JComboBox comboBox_3 = null;
	JComboBox comboBox_4 = null;
	JComboBox comboBox_5 = null;
	JComboBox comboBox_6 = null;
	JComboBox comboBox_7 = null;
	JButton btnExeCmd = null;
	JButton btnNewButton = null;
	JButton btnNewButton_1 = null;
	JButton btnNewButton_2 = null;
	JButton btnNewButton_3 = null;
	JButton btnNewButton_4 = null;
	JButton btnNewButton_5 = null;
	JButton btnNewButton_6 = null;
	JButton btnNewButton_7 = null;
	JPanel contentPane = null;
	JTextField txtx = null;
	JTextField txtx_1 = null;
	JTextField txtx_2 = null;
	JTextField txtx_3 = null;
	JTextField txtx_4 = null;
	JTextField txtx_5 = null;
	JTextField txtRawxx = null;
	JLabel lblNewLabel_3 = null;
	JLabel lblNewLabel_6 = null;
	JRadioButton rdbtnNewRadioButton = null;
	JRadioButton rdbtnSensorId = null;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					HyperscaleSensorTestTool frame = new HyperscaleSensorTestTool();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public HyperscaleSensorTestTool() {
		setTitle("Sensor Test Tool For Hyperscale");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 767, 434);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setBounds(10, 25, 600, 180);
		contentPane.add(scrollPane);
		
		textArea = new JTextArea();
		textArea.setForeground(Color.BLUE);
		scrollPane.setViewportView(textArea);
		
		JLabel lblNewLabel = new JLabel("Test Result:");
		lblNewLabel.setForeground(Color.BLUE);
		lblNewLabel.setBounds(12, 5, 88, 18);
		contentPane.add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("IP:");
		lblNewLabel_1.setForeground(Color.BLUE);
		lblNewLabel_1.setBounds(620, 10, 54, 15);
		contentPane.add(lblNewLabel_1);
		
		comboBox = new JComboBox();
		comboBox.setForeground(Color.BLUE);
		comboBox.setModel(new DefaultComboBoxModel(new String[] {"111.111.111.111", "10.145.2.6", "10.245.19.169"}));
		comboBox.setEditable(true);
		comboBox.setBounds(620, 30, 120, 20);
		contentPane.add(comboBox);
		
		JLabel lblUserid = new JLabel("USERID:");
		lblUserid.setForeground(Color.BLUE);
		lblUserid.setBounds(620, 60, 54, 15);
		contentPane.add(lblUserid);
		
		comboBox_1 = new JComboBox();
		comboBox_1.setModel(new DefaultComboBoxModel(new String[] {"USERID", "ADMIN", "Userid"}));
		comboBox_1.setForeground(Color.BLUE);
		comboBox_1.setEditable(true);
		comboBox_1.setBounds(620, 80, 120, 20);
		contentPane.add(comboBox_1);
		
		JLabel lblPassword = new JLabel("PASSWORD:");
		lblPassword.setForeground(Color.BLUE);
		lblPassword.setBounds(620, 110, 78, 15);
		contentPane.add(lblPassword);
		
		comboBox_2 = new JComboBox();
		comboBox_2.setModel(new DefaultComboBoxModel(new String[] {"PASSW0RD", "Passw0rd"}));
		comboBox_2.setForeground(Color.BLUE);
		comboBox_2.setEditable(true);
		comboBox_2.setBounds(620, 130, 120, 20);
		contentPane.add(comboBox_2);
		
		JLabel lblInterface = new JLabel("INTERFACE:");
		lblInterface.setForeground(Color.BLUE);
		lblInterface.setBounds(620, 160, 88, 15);
		contentPane.add(lblInterface);
		
		comboBox_3 = new JComboBox();
		comboBox_3.setModel(new DefaultComboBoxModel(new String[] {"lanp", "lan"}));
		comboBox_3.setForeground(Color.BLUE);
		comboBox_3.setEditable(true);
		comboBox_3.setBounds(620, 180, 120, 20);
		contentPane.add(comboBox_3);
		
		JPanel panel = new JPanel();
		panel.setBounds(620, 210, 125, 180);
		contentPane.add(panel);
		panel.setLayout(null);
		
		rdbtnNewRadioButton = new JRadioButton("Sensor Name:");
		rdbtnNewRadioButton.setForeground(Color.BLUE);
		rdbtnNewRadioButton.setBounds(0, 0, 121, 23);
		panel.add(rdbtnNewRadioButton);
		
		comboBox_4 = new JComboBox();
		comboBox_4.setModel(new DefaultComboBoxModel(new String[] {"null"}));
		comboBox_4.setForeground(Color.BLUE);
		comboBox_4.setToolTipText("Sensor Name\u548CSensor ID\u4F1A\u81EA\u52A8\u4ECEBMC\u83B7\u53D6\u3002\r\n\u65F6\u95F4\u53EF\u80FD\u6709\u4E9B\u957F\u3002\r\n\u8BF7\u7A0D\u7B49\u3002");
		comboBox_4.setEditable(true);
		comboBox_4.setBounds(0, 25, 120, 20);
		panel.add(comboBox_4);
		
		rdbtnSensorId = new JRadioButton("Sensor ID:");
		rdbtnSensorId.setForeground(Color.BLUE);
		rdbtnSensorId.setBounds(0, 51, 121, 23);
		panel.add(rdbtnSensorId);
		
		comboBox_5 = new JComboBox();
		comboBox_5.setModel(new DefaultComboBoxModel(new String[] {"null"}));
		comboBox_5.setForeground(Color.BLUE);
		comboBox_5.setEditable(true);
		comboBox_5.setBounds(0, 80, 120, 20);
		panel.add(comboBox_5);
		
		btnNewButton = new JButton("Run Test");
		btnNewButton.setForeground(Color.BLUE);
		btnNewButton.setToolTipText("\u5F00\u59CB\u6D4B\u8BD5\u3002");
		btnNewButton.setBounds(1, 134, 120, 30);
		panel.add(btnNewButton);
		
		JLabel lblRunTest = new JLabel("Run Test:");
		lblRunTest.setForeground(Color.BLUE);
		lblRunTest.setBounds(0, 110, 54, 15);
		panel.add(lblRunTest);
		
		JPanel panel_1 = new JPanel();
		panel_1.setBounds(10, 329, 600, 70);
		contentPane.add(panel_1);
		panel_1.setLayout(null);
		
		btnNewButton_1 = new JButton("DC Server");
		btnNewButton_1.setForeground(Color.BLUE);
		btnNewButton_1.setToolTipText("\u91CD\u542F\u670D\u52A1\u5668\u3002");
		btnNewButton_1.setBounds(17, 5, 93, 23);
		panel_1.add(btnNewButton_1);
		
		btnNewButton_2 = new JButton("Reset BMC");
		btnNewButton_2.setForeground(Color.BLUE);
		btnNewButton_2.setToolTipText("\u91CD\u542FBMC\u3002");
		btnNewButton_2.setBounds(115, 5, 93, 23);
		panel_1.add(btnNewButton_2);
		
		btnNewButton_3 = new JButton("Clear SEL");
		btnNewButton_3.setForeground(Color.BLUE);
		btnNewButton_3.setToolTipText("\u6E05\u9664UEFI\u65E5\u5FD7\u3002");
		btnNewButton_3.setBounds(213, 5, 93, 23);
		panel_1.add(btnNewButton_3);
		
		btnNewButton_4 = new JButton("Clear RST");
		btnNewButton_4.setForeground(Color.BLUE);
		btnNewButton_4.setToolTipText("\u6E05\u9664\u5C4F\u5E55\u8F93\u51FA\u7ED3\u679C\u3002");
		btnNewButton_4.setBounds(311, 5, 93, 23);
		panel_1.add(btnNewButton_4);
		
		btnNewButton_5 = new JButton("Get SEL ");
		btnNewButton_5.setForeground(Color.BLUE);
		btnNewButton_5.setToolTipText("\u83B7\u53D6UEFI\u7684\u65E5\u5FD7\u3002");
		btnNewButton_5.setBounds(409, 5, 93, 23);
		panel_1.add(btnNewButton_5);
		
		btnNewButton_6 = new JButton("DST/THD");
		btnNewButton_6.setForeground(Color.BLUE);
		btnNewButton_6.setToolTipText("\u5207\u6362Sensor\u7684\u79CD\u7C7B\u3002");
		btnNewButton_6.setBounds(507, 5, 93, 23);
		panel_1.add(btnNewButton_6);
		
		JLabel lblExeIpmiCmd = new JLabel("Exe IPMI CMD:");
		lblExeIpmiCmd.setForeground(Color.BLUE);
		lblExeIpmiCmd.setBounds(17, 38, 93, 15);
		panel_1.add(lblExeIpmiCmd);
		
		txtRawxx = new JTextField();
		txtRawxx.setText("raw 0x06 0x01");
		txtRawxx.setForeground(Color.MAGENTA);
		txtRawxx.setBounds(115, 35, 387, 21);
		panel_1.add(txtRawxx);
		txtRawxx.setColumns(10);
		
		btnExeCmd = new JButton("Exe CMD");
		btnExeCmd.setForeground(Color.BLUE);
		btnExeCmd.setBounds(507, 34, 93, 23);
		panel_1.add(btnExeCmd);
		
		panel_2 = new JPanel();
		panel_2.setBounds(10, 210, 600, 122);
		contentPane.add(panel_2);
		panel_2.setLayout(null);
		
		JLabel lblThresholdSensors = new JLabel("Threshold Sensors:");
		lblThresholdSensors.setForeground(Color.BLUE);
		lblThresholdSensors.setBounds(10, 0, 122, 15);
		panel_2.add(lblThresholdSensors);
		
		JLabel lblNewLabel_2 = new JLabel("LNC:");
		lblNewLabel_2.setForeground(Color.BLUE);
		lblNewLabel_2.setBounds(30, 20, 54, 15);
		panel_2.add(lblNewLabel_2);
		
		txtx = new JTextField();
		txtx.setForeground(Color.MAGENTA);
		txtx.setText("0x00");
		txtx.setBounds(50, 40, 70, 21);
		panel_2.add(txtx);
		txtx.setColumns(10);
		
		JLabel lblUnc = new JLabel("UNC:");
		lblUnc.setForeground(Color.BLUE);
		lblUnc.setBounds(30, 70, 54, 15);
		panel_2.add(lblUnc);
		
		txtx_1 = new JTextField();
		txtx_1.setText("0x00");
		txtx_1.setForeground(Color.MAGENTA);
		txtx_1.setBounds(50, 90, 70, 21);
		panel_2.add(txtx_1);
		txtx_1.setColumns(10);
		
		lblNewLabel_3 = new JLabel("(LNC: 0x00,  LC: 0x00,  LCR: 0x00,  UNC: 0x00,  UC: 0x00,  UCR: 0x00)");
		lblNewLabel_3.setForeground(Color.MAGENTA);
		lblNewLabel_3.setBounds(147, 0, 443, 15);
		panel_2.add(lblNewLabel_3);
		
		JLabel lblLc = new JLabel("lC:");
		lblLc.setForeground(Color.BLUE);
		lblLc.setBounds(130, 20, 54, 15);
		panel_2.add(lblLc);
		
		txtx_2 = new JTextField();
		txtx_2.setText("0x00");
		txtx_2.setForeground(Color.MAGENTA);
		txtx_2.setBounds(150, 40, 70, 21);
		panel_2.add(txtx_2);
		txtx_2.setColumns(10);
		
		JLabel lblUc = new JLabel("UC:");
		lblUc.setForeground(Color.BLUE);
		lblUc.setBounds(130, 70, 54, 15);
		panel_2.add(lblUc);
		
		txtx_3 = new JTextField();
		txtx_3.setText("0x00");
		txtx_3.setForeground(Color.MAGENTA);
		txtx_3.setBounds(150, 90, 70, 21);
		panel_2.add(txtx_3);
		txtx_3.setColumns(10);
		
		JLabel lblNewLabel_4 = new JLabel("LCR:");
		lblNewLabel_4.setForeground(Color.BLUE);
		lblNewLabel_4.setBounds(230, 20, 54, 15);
		panel_2.add(lblNewLabel_4);
		
		txtx_4 = new JTextField();
		txtx_4.setText("0x00");
		txtx_4.setForeground(Color.MAGENTA);
		txtx_4.setBounds(250, 40, 70, 21);
		panel_2.add(txtx_4);
		txtx_4.setColumns(10);
		
		txtx_5 = new JTextField();
		txtx_5.setText("0x00");
		txtx_5.setForeground(Color.MAGENTA);
		txtx_5.setBounds(250, 90, 70, 21);
		panel_2.add(txtx_5);
		txtx_5.setColumns(10);
		
		JLabel lblNewLabel_5 = new JLabel("UCR:");
		lblNewLabel_5.setForeground(Color.BLUE);
		lblNewLabel_5.setBounds(230, 70, 54, 15);
		panel_2.add(lblNewLabel_5);
		
		JLabel lblCurrentReading = new JLabel("Current Reading:");
		lblCurrentReading.setForeground(Color.BLUE);
		lblCurrentReading.setBounds(360, 56, 107, 15);
		panel_2.add(lblCurrentReading);
		
		lblNewLabel_6 = new JLabel("0x00");
		lblNewLabel_6.setForeground(Color.MAGENTA);
		lblNewLabel_6.setBounds(464, 56, 54, 15);
		panel_2.add(lblNewLabel_6);
		
		btnNewButton_7 = new JButton("Refresh Reading");
		btnNewButton_7.setForeground(Color.BLUE);
		btnNewButton_7.setBounds(447, 89, 93, 23);
		panel_2.add(btnNewButton_7);
		
		panel_3 = new JPanel();
		panel_3.setBounds(10, 445, 600, 122);
		//contentPane.add(panel_3);
		panel_3.setLayout(null);
		
		JLabel lblNewLabel_7 = new JLabel("Discrete Sensors:");
		lblNewLabel_7.setForeground(Color.BLUE);
		lblNewLabel_7.setBounds(10, 0, 144, 15);
		panel_3.add(lblNewLabel_7);
		
		JLabel lblNewLabel_8 = new JLabel("Event Offset:");
		lblNewLabel_8.setForeground(Color.BLUE);
		lblNewLabel_8.setBounds(100, 25, 150, 15);
		panel_3.add(lblNewLabel_8);
		
		comboBox_6 = new JComboBox();
		comboBox_6.setModel(new DefaultComboBoxModel(new String[] {"null"}));
		comboBox_6.setForeground(Color.MAGENTA);
		comboBox_6.setEditable(true);
		comboBox_6.setBounds(125, 50, 170, 20);
		panel_3.add(comboBox_6);
		
		JLabel lblStatus = new JLabel("Status:");
		lblStatus.setForeground(Color.BLUE);
		lblStatus.setBounds(325, 25, 54, 15);
		panel_3.add(lblStatus);
		
		comboBox_7 = new JComboBox();
		comboBox_7.setModel(new DefaultComboBoxModel(new String[] {"null"}));
		comboBox_7.setForeground(Color.MAGENTA);
		comboBox_7.setEditable(true);
		comboBox_7.setBounds(350, 50, 120, 20);
		panel_3.add(comboBox_7);
		
		JLabel lblNewLabel_9 = new JLabel("\u54C8\u54C8\u54C8\u54C8\uFF0C\u754C\u9762\u5C31\u8FD9\u4E48\u5927\u3002");
		lblNewLabel_9.setForeground(Color.MAGENTA);
		lblNewLabel_9.setBounds(1217, 700, 190, 15);
		contentPane.add(lblNewLabel_9);
	}
}
